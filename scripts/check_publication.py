"""Reject tracked files outside the reviewed public release."""

import subprocess
from pathlib import Path

ALLOWED = {
    ".gitignore",
    "LICENSE",
    "README.md",
    "docs/methodology.md",
    "docs/publication-scope.md",
    "scripts/check_publication.py",
    "shared/__init__.py",
    "shared/tools/__init__.py",
    "shared/tools/_paths.py",
    "shared/tools/logger.py",
    "shared/tools/text_chunker.py",
    "tests/test_utilities.py",
}


def main():
    root = Path(__file__).resolve().parents[1]
    git_root = Path(subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"], cwd=root, text=True
    ).strip()).resolve()
    if git_root != root:
        raise SystemExit("Run this check in the standalone public repository.")
    records = subprocess.check_output(
        ["git", "ls-files", "--stage", "-z"], cwd=root
    ).decode().split("\0")
    paths = set()
    problems = []
    for record in filter(None, records):
        metadata, path = record.split("\t", 1)
        mode, _, stage = metadata.split()
        paths.add(path)
        if mode != "100644" or stage != "0":
            problems.append(f"Unexpected index entry: {path}")
        if (root / path).is_symlink():
            problems.append(f"Symbolic link: {path}")
    problems.extend(f"Unreviewed path: {p}" for p in sorted(paths - ALLOWED))
    problems.extend(f"Missing release file: {p}" for p in sorted(ALLOWED - paths))
    if problems:
        raise SystemExit("\n".join(problems))
    print(f"PASS: {len(paths)} reviewed regular files; no submodules or symbolic links.")


if __name__ == "__main__":
    main()
