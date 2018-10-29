"""
Contains server config
"""
import os
import logging

from dp4py_config.section import Section
from dp4py_config.utils import bool_env


CONFIG = Section("Global config")

CONFIG.APP = Section("APP config")
CONFIG.APP.title = 'dp4py-sanic'
CONFIG.APP.description = 'Sanic app wrapper for digital publishing that implements JSON logging'

CONFIG.LOGGING = Section("Logging config")
CONFIG.LOGGING.namespace = os.environ.get("LOGGING_NAMESPACE", CONFIG.APP.title)
CONFIG.LOGGING.default_level = logging.INFO
CONFIG.LOGGING.coloured_logging = bool_env('COLOURED_LOGGING_ENABLED', False)
CONFIG.LOGGING.pretty_logging = bool_env('PRETTY_LOGGING', False)
CONFIG.LOGGING.json_logger_indent = 4 if CONFIG.LOGGING.pretty_logging else None
