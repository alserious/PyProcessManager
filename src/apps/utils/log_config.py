import os
import logging
from sys import stdout


def log_config(name: str, debug: bool = False) -> logging.Logger:
    log_level = str(os.getenv("LOG_LEVEL_APPS", "INFO")).upper()

    if debug:
        log_level = "DEBUG"

    logFormatter = logging.Formatter(
        "%(asctime)s:%(levelname)s:%(module)s:%(name)s:%(message)s"
    )

    consoleHandler = logging.StreamHandler(stdout)
    consoleHandler.setFormatter(logFormatter)

    level = logging.getLevelName(log_level)
    logging.basicConfig(level=level, handlers=[consoleHandler])
    logger = logging.getLogger(name)

    return logger
