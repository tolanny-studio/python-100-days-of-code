from termcolor import cprint
import logging
from validate import validate_number
from tipcalculator import TipCalculator

logger = logging.getLogger(__name__)

TOTAL_BILL_PROMPT = "\nWhat was the total bill ? "
PERCENTAGE_TIP_PROMPT = "\nWhat percentage tip would you like to give ? "
BILL_SPLITTERS = "\nHow many people to split the bill ? "


def get_total_bill() -> float:
    return validate_number(input(TOTAL_BILL_PROMPT))


def get_percentage_tip() -> float:
    return validate_number(input(PERCENTAGE_TIP_PROMPT))


def get_bill_splitters() -> int:
    return int(validate_number(input(BILL_SPLITTERS)))


def main():
    cprint("Welcome to the tip calculator", "light_blue")
    total_bill = get_total_bill()
    percentage_tip = get_percentage_tip()
    bill_splitters = get_bill_splitters()
    tip_calculator = TipCalculator(total_bill, percentage_tip, bill_splitters)
    cprint(tip_calculator, "light_green")


if __name__ == "__main__":
    main()
