from termcolor import cprint

import logging
import logging_config

from validate import validate_number, validate_splitters
from tipcalculator import TipCalculator

logger = logging.getLogger(__name__)

TOTAL_BILL_PROMPT = "\nWhat was the total bill ? "
PERCENTAGE_TIP_PROMPT = "\nWhat percentage tip would you like to give ? "
BILL_SPLITTERS_PROMPT = "\nHow many people to split the bill ? "

"""
Entry point for the Tip Calculator application.

This module collects user input, validates it,
creates a TipCalculator instance, and displays
the calculated payment.
"""


def get_total_bill() -> float:
    """
    Prompt until a valid total bill amount is entered.

    Returns:
        float: Validated bill amount.
    """
    while True:
        total_bill = input(TOTAL_BILL_PROMPT)
        validated_total_bill = validate_number(total_bill)
        if validated_total_bill is None:
            continue
        return validated_total_bill


def get_percentage_tip() -> float:
    """
    Prompt until a valid tip percentage is entered.

    Returns:
        float: Validated tip percentage.
    """
    while True:
        percentage_tip = input(PERCENTAGE_TIP_PROMPT)
        validated_percentage_tip = validate_number(percentage_tip)
        if validated_percentage_tip is None:
            continue
        return validated_percentage_tip


def get_bill_splitters() -> int:
    """
    Prompt until a valid number of bill splitters is entered.

    Returns:
        int: Number of people sharing the bill.
    """
    while True:
        bill_splitters = input(BILL_SPLITTERS_PROMPT)
        validated_bill_splitters = validate_splitters(bill_splitters)
        if validated_bill_splitters is None:
            continue
        return validated_bill_splitters


def main() -> None:
    """
    Run the Tip Calculator application.

    Collects validated input, calculates each person's
    payment, and displays the result.
    """
    logger.info("Tip calculator started")
    cprint("Welcome to the tip calculator", "light_blue")
    total_bill = get_total_bill()
    percentage_tip = get_percentage_tip()
    bill_splitters = get_bill_splitters()
    tip_calculator = TipCalculator(total_bill, percentage_tip, bill_splitters)
    cprint(tip_calculator, "light_green")


if __name__ == "__main__":
    main()
