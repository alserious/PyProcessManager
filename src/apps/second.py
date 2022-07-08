import os
import time
import sys

from .utils import log_config

# logger = log_config(str(__name__))


def main():
    # logger.info(f"Start: {sys.modules[__name__]}")
    # time.sleep(10)
    # logger.info(f"End: {sys.modules[__name__]}")
    print("ok")
    print(os.getcwd())
    print(os.environ)


if __name__ == "__main__":
    main()
