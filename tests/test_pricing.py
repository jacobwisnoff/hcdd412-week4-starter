"""
Starter tests for src/pricing.py

NOTE FOR STUDENTS: these tests only check the "happy path" — normal,
well-formed input. That's intentional. Part of this week's assignment
is using GitHub Copilot's Test Generation feature to add tests that go
further: edge cases, boundary conditions, and failure scenarios. See
the Week 4 Canvas Module for the full assignment instructions.
"""

from src.pricing import calculate_discount, apply_bulk_discount


def test_calculate_discount_happy_path():
    assert calculate_discount(100, 20) == 80.0


def test_apply_bulk_discount_happy_path():
    # 5 units at $10 each, below the default threshold of 10 — no discount applied
    assert apply_bulk_discount(10, 5) == 50.0


# TODO (assignment): use GitHub Copilot to generate additional tests here.
# Prompt iteratively toward:
#   - edge cases       (e.g., price = 0, percent_off = 0, quantity = 0)
#   - boundary conditions (e.g., percent_off = 100, quantity exactly at threshold)
#   - failure scenarios (e.g., negative price, percent_off = 150, negative quantity)
#
# Document your prompts and iterations in your submitted reflection.
def test_calculate_discount_zero_price():
    assert calculate_discount(0, 20) == 0.0


def test_calculate_discount_zero_percent():
    assert calculate_discount(100, 0) == 100.0


def test_calculate_discount_one_hundred_percent():
    assert calculate_discount(100, 100) == 0.0


def test_calculate_discount_rounds_to_two_decimal_places():
    assert calculate_discount(10, 33.333) == 6.67


def test_calculate_discount_rejects_negative_price():
    try:
        calculate_discount(-1, 20)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for negative price"


def test_calculate_discount_rejects_percent_above_one_hundred():
    try:
        calculate_discount(100, 100.01)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for percent_off above 100"


def test_calculate_discount_rejects_percent_off_of_150():
    try:
        calculate_discount(100, 150)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for percent_off of 150"


def test_calculate_discount_rejects_negative_percent():
    try:
        calculate_discount(100, -1)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for negative percent_off"


def test_apply_bulk_discount_quantity_exactly_at_threshold():
    assert apply_bulk_discount(10, 10) == 100.0


def test_apply_bulk_discount_quantity_above_threshold():
    assert apply_bulk_discount(10, 11) == 93.5
