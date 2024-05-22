import logging

logger = logging.getLogger("fastapi")

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(asctime)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Suppress pymongo debug logs
logging.getLogger("pymongo").setLevel(logging.WARNING)
