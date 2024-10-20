import logging

from rich.logging import RichHandler


fmt = "%(asctime)s - %(message)s"

logging.basicConfig(
    level="WARNING",
    format=fmt,
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

logger = logging.getLogger(__name__)
