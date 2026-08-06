from pathlib import Path
import logging
"""
Application logging configuration.
This module configures the application's logging system.
Importing this module once initializes logging for all
other modules in the application.
"""

LOG_FILE = Path(__file__).parent / "tip_calculator.log"

logging.basicConfig(
    filename=LOG_FILE,
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    force=True,
)