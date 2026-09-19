# HCDD 412 — Week 4 Starter: CI Pipeline with Automated Unit Tests

This is the starting point for the Week 4 lab: **CI Pipeline with Automated Unit Tests**.
Stack: **Python 3**, **pytest**, and **flake8** — no cloud services, databases, or
external accounts required. Everything here runs entirely on your own machine.

## What's in this repo

```
hcdd412-week4-starter/
├── .github/workflows/ci.yml   # GitHub Actions: lints and tests on every push/PR
├── src/
│   ├── pricing.py              # discount calculation functions
│   └── csv_utils.py            # simple CSV row parsing functions
├── tests/
│   ├── test_pricing.py         # starter tests — happy path only
│   └── test_csv_utils.py       # starter tests — happy path only
├── requirements.txt             # runtime dependencies (none — stdlib only)
├── requirements-dev.txt         # pytest + flake8
├── pytest.ini                   # scopes test discovery to tests/
└── .flake8                      # lint rules
```

## Setup (local, one time)

```bash
# 1. Clone your copy of this repo, then from its root:
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Running things locally

```bash
# Run the test suite
pytest

# Run the linter
flake8 src tests
```

Both of these are exactly what the GitHub Actions workflow runs on every push and
pull request — if they pass locally, they'll pass in CI.

## The assignment

The starter tests in `tests/` **only check the happy path** — normal, well-formed
input. That's intentional. Open `src/pricing.py` and `src/csv_utils.py`, read the
docstrings, and notice what's *not* being tested yet.

Your job:

1. Use **GitHub Copilot's Test Generation** feature (right-click a function →
   *Generate Tests*, or Copilot Chat's `/tests`) to generate additional test
   cases for these functions.
2. **Don't stop at Copilot's first draft.** It will likely give you more
   happy-path tests. Prompt it again, specifically, toward:
   - **Edge cases** — empty input, zero, `None`
   - **Boundary conditions** — values exactly at a threshold or limit
   - **Failure scenarios** — invalid input that should raise an error
3. Review every generated test before you keep it — ask yourself whether it
   actually *proves* something about the function's behavior, or whether it's
   just another version of the same happy-path check.
4. Commit your work and push. Confirm the **CI workflow passes** (green check)
   on GitHub.
5. Submit, per the Week 4 Canvas Module: your repository link, a screenshot of
   the passing GitHub Actions run, and your 300-word reflection on your
   Copilot prompting process — including at least one test you rejected or
   rewrote.

A hint, from the lecture: `apply_bulk_discount`'s discount only triggers when
quantity is *strictly greater than* the threshold. Is that the right boundary?
A boundary test will show you exactly what happens at `quantity == threshold` —
decide for yourself whether that's a bug worth flagging in your reflection.

## Troubleshooting

- **`ModuleNotFoundError: No module named 'src'`** — run `pytest` from the
  repository root, not from inside `tests/`.
- **flake8 complains about line length** — the configured limit is 100
  characters (see `.flake8`); wrap long lines rather than suppressing the rule.
- **CI is red but tests pass locally** — check you committed both
  `requirements.txt` and `requirements-dev.txt`, and that you're not relying on
  a package installed locally but not listed in either file.
