import logging
logging.basicConfig(
    filename="tip_calculator.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

logger = logging.getLogger(__name__)