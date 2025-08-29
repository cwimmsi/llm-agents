import logging
import os
import re
from datetime import datetime
from colorama import Fore, Style

GLOBAL_LOGGER_NAME = "llm-agents"
GLOBAL_LOG_FILE_NAME = "llm-agents"


class ColorFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: Fore.BLUE,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
    }

    def format(self, record):
        color = self.COLORS.get(record.levelno, Fore.WHITE)
        message = super().format(record)
        return f"{color}{message}{Style.RESET_ALL}"


def setup_logger() -> logging.Logger:
    # Create a logger
    logger = logging.getLogger(GLOBAL_LOGGER_NAME)

    # Only add console handlers if logger doesn't have handlers
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        # Create console handler and set level to info
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create file handler and set level to debug
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # Replace invalid characters (e.g., :, /, \, *, ?, ", <, >, |) with an underscore
        safe_logger_name = re.sub(r'[<>:"/\\|?*]', "_", GLOBAL_LOGGER_NAME)
        safe_log_file_name = re.sub(r'[<>:"/\\|?*]', "_", GLOBAL_LOG_FILE_NAME)
        # Build final log file path
        log_file = f"logs/{safe_logger_name}/{safe_log_file_name}_{timestamp}.log"
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)

        # Create formatters
        console_formatter = ColorFormatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )
        file_formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )

        # Set formatters for handlers
        console_handler.setFormatter(console_formatter)
        file_handler.setFormatter(file_formatter)

        # Add handlers to logger
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger


def set_logger_name_and_log_file_name(logger_name: str, log_file_name: str):
    global GLOBAL_LOGGER_NAME, GLOBAL_LOG_FILE_NAME
    GLOBAL_LOGGER_NAME = logger_name
    GLOBAL_LOG_FILE_NAME = log_file_name
