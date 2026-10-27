# Research Paper: Elementary Number Theory and Public-Key Cryptography

LaTeX source and Python verification code for a B.Sc (Mathematics) research project.

## Status

| Part | Status |
|------|--------|
| Skeleton (`main.tex`, cover, certificate, bibliography) | Done |
| Ch 1 Introduction, Ch 2 Preliminaries | Drafted, needs author review |
| Ch 3 to Ch 8 | Stubs, to be drafted |
| Python routines and tests (`code/`) | Done for sieve, gcd, extended gcd, modpow |

## Build

Requires a TeX distribution with `biber` (for `biblatex`):

```
cd research-paper
latexmk -pdf main.tex
```

## Test the code

```
python -m pytest research-paper/code
```

## Before submission

- Replace every `[bracketed]` placeholder on the cover, certificate and declaration.
- Verify each reference in `references.bib` against the book or journal. Do not submit an unchecked citation.
- Rewrite the drafted text in your own words and check every proof and example by hand.
- Check the UPRTOU format and originality rules with your guide.
