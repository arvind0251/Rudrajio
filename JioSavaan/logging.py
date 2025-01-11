import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.DEBUG,  # Changed log level to DEBUG for detailed logging.
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(module)s:%(lineno)d - %(message)s",  # Added module and line number.
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("log.txt", maxBytes=1000000, backupCount=3),  # Use rotating file handler.
        logging.StreamHandler(),
    ],
)

# Set log level to ERROR for specific libraries to reduce noise in logs.
logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pymongo").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
