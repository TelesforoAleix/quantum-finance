"""Offline checks using synthetic text and temporary log storage."""

import json
import logging
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

_temporary = tempfile.TemporaryDirectory()
_environment = patch.dict(os.environ, {"QUANTUM_FINANCE_PROJECT_ROOT": _temporary.name})
_environment.start()

from shared.tools import text_chunker
from shared.tools._paths import find_project_root
from shared.tools.logger import get_logger


def tearDownModule():
    logging.shutdown()
    _environment.stop()
    _temporary.cleanup()


class UtilityTests(unittest.TestCase):
    def setUp(self):
        self.encoder = patch.object(text_chunker, "_get_encoder", return_value=None)
        self.encoder.start()
        self.addCleanup(self.encoder.stop)

    def test_truncation_budget(self):
        self.assertEqual(text_chunker.truncate_tokens("abcdefghijkl", 2), "abcdefgh")
        self.assertEqual(text_chunker.truncate_tokens("short", 20), "short")

    def test_disabled_budget_preserves_input(self):
        text = "# Heading\n\nExample text."
        self.assertEqual(text_chunker.chunk_by_sections(text, 0), [text])
        self.assertEqual(text_chunker.truncate_tokens(text, 0), text)

    def test_long_word_preserved_across_chunks(self):
        text = "abcdefghij" * 30
        chunks = text_chunker.chunk_by_sections(text, 7)
        self.assertEqual("".join(chunks), text)
        self.assertTrue(all(len(chunk) <= 28 for chunk in chunks))

    def test_sections_preserve_words_and_budget(self):
        text = "# One\nSynthetic sample text.\n# Two\nMore synthetic text."
        chunks = text_chunker.chunk_by_sections(text, 8)
        self.assertEqual(" ".join(chunks).split(), text.split())
        self.assertTrue(all(len(chunk) <= 32 for chunk in chunks))

    def test_root_override(self):
        self.assertEqual(find_project_root(), Path(_temporary.name))

    def test_logging_is_structured_and_handlers_are_reused(self):
        logger = get_logger("public_test")
        count = len(logger.handlers)
        self.assertIs(get_logger("public_test"), logger)
        self.assertEqual(len(logger.handlers), count)
        logger.info("Synthetic test event", extra={"stage": "test"})
        for handler in logger.handlers:
            handler.flush()
        path = next((Path(_temporary.name) / "logs").glob("*_public_test.jsonl"))
        record = json.loads(path.read_text().splitlines()[-1])
        self.assertEqual(record["message"], "Synthetic test event")
        self.assertEqual(record["stage"], "test")
        self.assertIn("git_sha", record)


if __name__ == "__main__":
    unittest.main()
