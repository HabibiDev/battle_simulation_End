import logging


def mylogger(session, logger_level):
    if logger_level == 'debug':
        logger1 = logging.getLogger('debug')
        logHandler = logging.FileHandler(session + "_debug.log")
        formatter = logging.Formatter(
            '%(asctime)-15s:%(levelname)s:%(message)s')
    elif logger_level == 'info':
        logger1 = logging.getLogger('info')
        logHandler = logging.FileHandler(session + "_Armies.log")
        formatter = logging.Formatter('%(levelname)s:%(message)s')
    logHandler.setFormatter(formatter)
    logger1.addHandler(logHandler)
    if logger_level == 'debug':
        logger1.setLevel(logging.DEBUG)
    elif logger_level == 'info':
        logger1.setLevel(logging.INFO)
    return logger1
