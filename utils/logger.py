import logging
from colorama import Fore, Style


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
    logger = logging.getLogger("llm_agents")

    # Only add handler if logger doesn't have handlers
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        # Create console handler and set level to info
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)

        # Create custom formatter
        formatter = ColorFormatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)

        # Add handler to logger
        logger.addHandler(handler)

    return logger
