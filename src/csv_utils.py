"""
csv_utils.py

Small CSV-row parsing utilities for the HCDD 412 Week 4 lab.

Like pricing.py, these functions are deliberately simple. The starter
tests only cover a well-formed row. Real CSV data is messy — empty
lines, missing values, unexpected delimiters — and it's your job this
week to generate tests (with Copilot) that prove these functions
actually handle that mess correctly, not just the clean case.
"""


def parse_csv_row(line, delimiter=","):
    """
    Split a single line of CSV text into a list of trimmed field values.

    Args:
        line (str): one line of CSV text (no trailing newline required).
        delimiter (str): the field delimiter. Defaults to a comma.

    Returns:
        list[str]: the fields in the row, each stripped of surrounding whitespace.

    Raises:
        ValueError: if line is None or, after stripping, empty.
    """
    if line is None:
        raise ValueError("line cannot be None")

    stripped = line.strip()
    if stripped == "":
        raise ValueError("line cannot be empty")

    return [field.strip() for field in stripped.split(delimiter)]


def validate_row_length(row, expected_length):
    """
    Check whether a parsed row has the expected number of fields.

    Args:
        row (list): a parsed CSV row, e.g. the output of parse_csv_row.
        expected_length (int): the number of fields the row should have.

    Returns:
        bool: True if len(row) == expected_length, False otherwise.
    """
    return len(row) == expected_length
