"""
Starter tests for src/csv_utils.py

NOTE FOR STUDENTS: same story as test_pricing.py — this only proves the
clean, well-formed case works. Real CSV input is messier than this.
Use Copilot to help you generate tests for the messy cases, then review
and iterate on what it gives you.
"""

from src.csv_utils import parse_csv_row, validate_row_length


def test_parse_csv_row_happy_path():
    assert parse_csv_row("a,b,c") == ["a", "b", "c"]


def test_validate_row_length_happy_path():
    row = ["a", "b", "c"]
    assert validate_row_length(row, 3) is True


# TODO (assignment): use GitHub Copilot to generate additional tests here.
# Prompt iteratively toward:
#   - edge cases       (e.g., empty line, whitespace-only fields, single field)
#   - boundary conditions (e.g., trailing delimiter creating an empty field)
#   - failure scenarios (e.g., line=None, line="", wrong delimiter used)
#
# Document your prompts and iterations in your submitted reflection.
