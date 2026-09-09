# Quantum Finance

Public edition of the parent research project for an MSc thesis on practical
quantum advantage in finance at Copenhagen Business School.

The research connects systematic literature review, structured extraction,
thematic synthesis, and assessment of quantum advantage claims. The practical
question is whether an advantage survives data preparation, resource costs,
and comparison with a classical baseline.

## Research Workflow

| Stage | Purpose |
| --- | --- |
| Framework synthesis | Develop a taxonomy for financial problems, quantum methods, and evidence. |
| Systematic review and classification | Identify studies and classify them against the framework. |
| Thematic synthesis | Compare findings within financial problem domains and across the corpus. |
| Experimental assessment | Examine resource estimates and advantage claims under explicit assumptions. |

The classified research corpus contains 777 papers. This public edition does
not redistribute that corpus or claim to reproduce the thesis results on its own.
See [methodology and limitations](docs/methodology.md).

## Related Repositories

The parent project brought together work developed in these earlier repositories:

| Repository | Role |
| --- | --- |
| [quantum-finance-slr](https://github.com/vallahrich/quantum-finance-slr) | Systematic-review toolkit: searching, ingestion, deduplication, screening, and topic coding. |
| [quantum-finance-analysis](https://github.com/TelesforoAleix/quantum-finance-analysis) | Earlier extraction and cross-paper analysis pipeline. |

These are separate repositories with their own history, dependencies, and setup
instructions. Their files are not bundled into this release, and this release's
publication review does not cover their contents or history.

## Included Utilities

This edition includes three reviewed Python utilities from the parent project:

- `shared/tools/text_chunker.py`: section-aware chunking and token-budget truncation.
- `shared/tools/logger.py`: structured local logging with revision metadata.
- `shared/tools/_paths.py`: project-root discovery with an environment override.

Python 3.12+ is the supported runtime. The default path uses only the standard
library and needs no API credentials. Token budgeting uses an approximate
four-characters-per-token fallback. An optional `tiktoken` installation enables
tokenizer-based counting; encoder loading may download tokenizer data.

```bash
git clone https://github.com/TelesforoAleix/quantum-finance.git
cd quantum-finance
python3 -m unittest discover -s tests -v
python3 -c "from shared.tools.text_chunker import chunk_by_sections; print(chunk_by_sections('Example research text.', max_tokens=8))"
```

Logs are written locally under `logs/` and are excluded from version control.

## Contributors

The thesis was co-authored by Aleix Moreno Telesforo
([TelesforoAleix](https://github.com/TelesforoAleix)) and Vincent Wallerich
([vallahrich](https://github.com/vallahrich)). Aleix was a substantial contributor
to the parent research repository. Its development history also credits
[superman32432432](https://github.com/superman32432432).

This edition starts with a new Git history, so its contributor graph does not
represent the original collaboration.

## Publication Scope

This is a curated code and documentation release. Papers, extracted article text,
manuscripts, reviewer material, research datasets, credentials, configurations,
caches, and generated model outputs are excluded. The original research history
is retained privately.

See [publication scope](docs/publication-scope.md) for the release boundary and
checks. Included code and documentation retain the original [MIT license](LICENSE).
