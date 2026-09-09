# Publication Scope

Prepared on 2026-09-09 as a separate repository with a new root commit.

Only the files listed in `scripts/check_publication.py` belong to this edition.
The imported source consists of the original MIT license and three manually
reviewed shared utilities. Documentation and synthetic tests were prepared for
this edition.

## Excluded Material

- Original Git history, branches, tags, issues, and attachments.
- Third-party papers, PDFs, extracted text, and bibliographic exports.
- Manuscripts, supervisor feedback, reviewer workbooks, and internal notes.
- Corpus records, screening decisions, experiment outputs, and prompt logs.
- Environment files, API credentials, private service endpoints, and library identifiers.
- Caches, archives, generated artifacts, and research configurations.

## Checks Before Each Push

```bash
python3 scripts/check_publication.py
python3 -m unittest discover -s tests -v
gitleaks dir . --redact --no-banner
gitleaks git . --redact --no-banner --log-opts="--all"
```

The file check rejects unreviewed tracked paths, symbolic links, and submodules.
Gitleaks checks for known secret patterns; it cannot establish publication rights
or guarantee the absence of every possible sensitive value. Review every changed
file before publishing, including changes to already allowed paths.

The scope of these checks is this repository. Linked repositories are independent
and were not sanitized as part of this release.
