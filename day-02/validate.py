import logging
from termcolor import cprint

logger = logging.getLogger(__name__)

"""
Validation utilities.

This module contains helper functions used to validate
numeric user input throughout the application.
"""


def validate_number(number: str) -> float | None:
    """
    Validate a positive decimal number.

    Args:
        number: User supplied string.

    Returns:
        float | None:
            A validated floating-point number if valid; otherwise None.
    """
    try:
        number_ = float(number)
    except ValueError as error:
        cprint(f"\nInvalid input {error}", "light_red", attrs=["italic"])
        logger.warning("\nInvalid input %s", error)
        return None
    if number_ <= 0:
        logger.warning("\nInput should be greater than 0")
        cprint("\nInput should be greater than 0", "light_red", attrs=["italic"])
        return None

    return number_


def validate_splitters(number: str) -> int | None:
    """
    Validate the number of bill splitters.

    The value must be a positive integer greater than zero.

    Args:
        number: User supplied string.

    Returns:
        int | None:
            A validated integer if valid; otherwise None.
    """

    try:
        number_ = int(number)
    except ValueError as error:
        logger.warning("\nInvalid input %s", error)
        cprint(f"\nInvalid input {error}", "light_red", attrs=["italic"])
        return None

    if number_ <= 0:
        logger.warning("\nSplitters should be greater than 0")
        cprint("\nSplitters should be greater than 0", "light_red", attrs=["italic"])
        return None
    return number_
