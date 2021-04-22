import logging
import sys

import colorlog


# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    def __init__(self):
        formatter = colorlog.ColoredFormatter(
            "%(log_color)s%(asctime)s - %(levelname)s (%(filename)s): %(message)s"
        )

        handler = colorlog.StreamHandler(
            sys.stdout,
        )
        handler.setFormatter(formatter)

        # This will affect any underlying library using python
        main_logger = colorlog.getLogger()
        main_logger.addHandler(handler)
        main_logger.setLevel(logging.INFO)

        # This is specifically for this application
        logger = colorlog.getLogger()

        self.logger = logger

    def __getattr__(self, attr):
        return getattr(self.logger, attr)
