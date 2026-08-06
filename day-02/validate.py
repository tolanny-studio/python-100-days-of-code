import logging

logger = logging.getLogger(__name__)


def validate_number(number: str) -> float:
    while True:
        try:
            number_ = float(input(number))
        except ValueError as error:
            logger.error("\nInvalid input %s", error)
            continue
        else:
            return number_
