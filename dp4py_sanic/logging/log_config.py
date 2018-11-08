"""
Initialises APP wide logging config
"""
import os
import logging

from dp4py_sanic.config import CONFIG
from dp4py_sanic.logging.formatter import SanicJsonFormatter

from dp4py_logging.loggers import DPLogger, TRACE
from dp4py_logging.config import config_for_formatter

# Set logger class
logging.addLevelName(TRACE, "TRACE")
logging.setLoggerClass(DPLogger)

# Set supported log keys
supported_keys = [
    'timestamp',
    'level',
    'pathname',
    'funcName',
    'lineno',
    'module',
    'message',
    'name',
    'pathname'
]


def get_level_name(level):
    """
    Return the textual representation of logging level 'level'.

    If the level is one of the predefined levels (CRITICAL, ERROR, WARNING,
    INFO, DEBUG) then you get the corresponding string. If you have
    associated levels with names using addLevelName then the name you have
    associated with 'level' is returned.

    If a numeric value corresponding to one of the defined levels is passed
    in, the corresponding string representation is returned.

    Otherwise, a NotImplementedError is raised
    """
    from logging import _levelToName, _nameToLevel
    # See Issues #22386, #27937 and #29220 for why it's this way
    result = _levelToName.get(level)
    if result is not None:
        return result
    result = _nameToLevel.get(level)
    if result is not None:
        return result
    raise NotImplementedError("Unknown log level: %s" % level)


def get_log_level(default: str="INFO"):
    """
    Returns the configured log level, and logs error if invalid
    :return:
    """
    level = os.environ.get("LOG_LEVEL", default)
    if isinstance(level, str):
        level = level.upper()

    try:
        return get_level_name(level)
    except NotImplementedError as e:
        logging.error("Caught exception parsing log level", exc_info=e)
        raise SystemExit()


# Define the logging config and set the log level
log_config = config_for_formatter(SanicJsonFormatter, supported_keys,
                                  level=get_log_level(default=CONFIG.LOGGING.default_level))
