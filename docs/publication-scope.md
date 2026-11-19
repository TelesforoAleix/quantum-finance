# Publication scope

## What this repository publishes

This repository is an exact mirror of the Zenodo record
[10.5281/zenodo.20179194](https://doi.org/10.5281/zenodo.20179194). The record holds the
supplementary archive of the MSc thesis *Quantum Computing in Financial Services*
(Copenhagen Business School, 2026). The Zenodo record is the final, citable version.

- [`submission/`](../submission/) holds every file of `QF_Repository_47199_20260514.zip`
  (md5 `ef5fd922e53a13d9b82b7078e0f55153`), unchanged. No file is edited, redacted, reformatted
  or removed.
- The files outside `submission/` are the visitor README, the diagrams in this folder, this
  document, the checksum list and the CI check.

## What the archive leaves out

The archive does not include the copyrighted source PDFs, the full-text transcripts of the
corpus papers or the thesis manuscript. [`submission/FAIR_USE.md`](../submission/FAIR_USE.md)
lists every exclusion, gives the reason, and tells how to get the originals by DOI.

## How exactness is checked

- [`SHA256SUMS`](../SHA256SUMS) holds the SHA-256 of all 15,408 files. It was generated from the
  unzipped archive. Paths are relative to `submission/` and sorted.
- Git stores the archive files as raw bytes. Some files have CRLF line endings, and the
  archive's own `.gitattributes` would otherwise change them.
- The [mirror workflow](../.github/workflows/mirror.yml) runs on every pull request and every
  push to `main`. It checks every checksum and checks that Git tracks exactly 15,408 files under
  `submission/`.

To check a local clone:

```bash
cd submission && shasum -a 256 -c --quiet ../SHA256SUMS
git ls-files submission | wc -l   # 15408
```
