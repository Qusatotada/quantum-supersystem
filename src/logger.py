import logging
from pathlib import Path

LOG_FILE = Path("quantum.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("quantum")
