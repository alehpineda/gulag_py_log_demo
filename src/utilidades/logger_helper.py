""" Logger Helper module. """

import logging
import sys
from datetime import date
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

# A pretty default logging format
DEFAULT_FORMAT = "%(asctime)s|%(levelname)s|%(name)s|%(funcName)s|%(message)s"
DEFAULT_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DEFAULT_TIME_ROTATION = "midnight"
DEFAULT_TIME_INTERVAL = 1


def get_logger(
    log_file: str = f"logs/log_{date.today()}.out",
    log_level: int = logging.INFO,
    console_level: int = logging.INFO,
    log_format: str = DEFAULT_FORMAT,
    log_time_format: str = DEFAULT_TIME_FORMAT,
    log_time_rotation: str = DEFAULT_TIME_ROTATION,
    log_time_interval: int = DEFAULT_TIME_INTERVAL,
    log_name: str = None,
) -> logging.Logger:
    """Funcion que regresa un root logger configurado

    Args:
        log_file (str, optional): _description_. Defaults to 'log.out'.
        log_level (int, optional): _description_. Defaults to logging.INFO.
        console_leve (int, optional): _description_. Defaults to logging.INFO.
        log_format (str, optional): _description_. Defaults to DEFAULT_FORMAT.
        log_time_format (str, optional): _description_. Defaults to DEFAULT_TIME_FORMAT.
        log_time_rotation (str, optional): _description_. Defaults to DEFAULT_TIME_ROTATION.
        log_time_interval (int, optional): _description_. Defaults to DEFAULT_TIME_INTERVAL.
        log_name (str, optional): _description_. Defaults to None.

    Returns:
        logging.Logger: _description_
    """

    # Setup new root logger
    new_logger = logging.getLogger(name=log_name)
    new_logger.setLevel(level=log_level)

    # Setup time format
    log_format = logging.Formatter(fmt=log_format, datefmt=log_time_format)

    # Setup stream handler - what we see in terminal. Has different log level than time and file handler.
    stream_handler = logging.StreamHandler(stream=sys.stdout)
    stream_handler.setLevel(level=console_level)
    stream_handler.setFormatter(fmt=log_format)
    new_logger.addHandler(hdlr=stream_handler)

    # Setup time handler - log file will rotate at midnight by default.
    time_handler = TimedRotatingFileHandler(
        filename=log_file, when=log_time_rotation, interval=log_time_interval
    )
    time_handler.setLevel(level=log_level)
    time_handler.setFormatter(fmt=log_format)
    new_logger.addHandler(hdlr=time_handler)

    # Return logger formateado
    return new_logger
