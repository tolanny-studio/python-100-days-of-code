from pathlib import Path
import logging

LOG_FILE = Path(__file__).parent / "tip_calculator.log"

logging.basicConfig(
    filename=LOG_FILE,
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    force=True,
)