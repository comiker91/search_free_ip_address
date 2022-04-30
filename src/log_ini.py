import logging

LEVEL = {
    "debug":logging.DEBUG,
    "info":logging.INFO,
    "warning":logging.WARNING,
    "error":logging.ERROR,
    "critical":logging.CRITICAL
}


def log_ini(config) -> logging.Logger:

    file_name = config.log_file
    level = LEVEL[config.log_level]
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
    datefmt='%m/%d/%Y %H:%M:%S'
    logging.basicConfig(
        filename=file_name,
        format=format,
        datefmt=datefmt,
        level=level
    )
    logger = logging.getLogger("IP Checker")
    return logger
