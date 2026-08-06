import logging
from termcolor import cprint

logger = logging.getLogger(__name__)


def validate_number(number: str) -> float:
    try:
        number_ = float(number)
    except ValueError as error:
        logger.warning("\nInvalid input %s", error)
        cprint(f"\nInvalid input {error}", "light_red", attrs=["italic"])

    else:
        return number_


def validate_splitters(number: str) -> int | None:
    int_number = int(number)
    if int_number <= 0:
        cprint("\nSplitters should be greater than 0", "light_red", attrs=["italic"])
        logger.warning("\nSplitters should be greater than 0")
        return None
    try:
        number_ = int_number
    except ValueError as error:
        logger.warning("\nInvalid input %s", error)
        cprint(f"\nInvalid input {error}", "light_red", attrs=["italic"])

    else:
        return number_
