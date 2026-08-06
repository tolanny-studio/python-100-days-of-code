"""
Tip calculator domain model.

This module contains the TipCalculator class, which
calculates how much each person should pay after
adding a percentage tip.
"""


class TipCalculator:
    """
    Calculate each person's share of a bill including tip.

    Args:
        total_bill: Total bill amount.
        percentage_tip: Percentage tip to add.
        bill_splitters: Number of people sharing the bill.
    """

    def __init__(self, total_bill: float, percentage_tip: float, bill_splitters: int):
        self.total_bill = total_bill
        self.percentage_tip = percentage_tip
        self.bill_splitters = bill_splitters

        """
        Initialize the calculator with bill details.
        """

    def calculate_payment(self) -> float:
        """
        Calculate the amount each person should pay.

        Returns:
            float: Individual payment rounded to two decimal places.
        """
        # Calculate the total amount including tip.
        return (
            (self.total_bill + ((self.percentage_tip / 100) * self.total_bill))
        ) / self.bill_splitters

    def __str__(self):
        """
        Return a formatted payment message.

        Returns:
            str: Human-readable payment summary.
        """
        return f"\nEach person should pay " f"${self.calculate_payment():.2f}"
