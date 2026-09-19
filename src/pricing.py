"""
pricing.py

Small pricing utility functions for the HCDD 412 Week 4 lab.

These functions are intentionally simple — the point of this week's lab
isn't the business logic, it's the test suite you build around it. The
starter tests in tests/test_pricing.py only check the "happy path."
Your job (see the Week 4 assignment) is to use GitHub Copilot's Test
Generation feature to add meaningful tests: edge cases, boundary
conditions, and failure scenarios.
"""


def calculate_discount(price, percent_off):
    """
    Apply a percentage discount to a price.

    Args:
        price (float): the original price. Must be >= 0.
        percent_off (float): the discount percentage. Must be between 0 and 100, inclusive.

    Returns:
        float: the discounted price, rounded to 2 decimal places.

    Raises:
        ValueError: if price is negative, or percent_off is outside [0, 100].
    """
    if price < 0:
        raise ValueError("price cannot be negative")
    if not 0 <= percent_off <= 100:
        raise ValueError("percent_off must be between 0 and 100")

    discounted = price * (1 - percent_off / 100)
    return round(discounted, 2)


def apply_bulk_discount(unit_price, quantity, threshold=10, discount_percent=15):
    """
    Calculate a total order price, applying a bulk discount once the
    quantity ordered exceeds a threshold.

    Args:
        unit_price (float): price of a single unit. Must be >= 0.
        quantity (int): number of units ordered. Must be >= 0.
        threshold (int): quantity that must be exceeded to trigger the discount.
        discount_percent (float): discount percentage applied once triggered.

    Returns:
        float: total order price, rounded to 2 decimal places.

    Raises:
        ValueError: if unit_price or quantity is negative.
    """
    if unit_price < 0:
        raise ValueError("unit_price cannot be negative")
    if quantity < 0:
        raise ValueError("quantity cannot be negative")

    total = unit_price * quantity
    if quantity > threshold:
        total -= total * (discount_percent / 100)

    return round(total, 2)
