import logging


def setup_logger() -> logging.Logger:
    # Create a logger
    logger = logging.getLogger("llm_agents")

    # Only add handler if logger doesn't have handlers
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        # Create console handler and set level to info
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)

        # Create formatter
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)

        # Add handler to logger
        logger.addHandler(handler)

    return logger
