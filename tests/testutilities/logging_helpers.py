import logging


def enable_console_logging(log=None, level=logging.DEBUG):
    logger = logging.getLogger(log)
    logger.setLevel(level=level)
    console_ch = logging.StreamHandler()
    logger.addHandler(console_ch)
    return logger
