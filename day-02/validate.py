import logging
from termcolor import cprint

logger = logging.getLogger(__name__)


def validate_number(number: str) -> float:
    try:
        number_ = float(number)
    except ValueError as error:
        logger.warning("\nInvalid input %s", error)
        cprint(f"\nInvalid input {error}","light_red",attrs=["italic"])

    else:
        return number_
