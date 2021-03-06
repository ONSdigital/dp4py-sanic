"""
Add namespace to all log messages
"""
from dp4py_sanic.config import CONFIG
from dp4py_logging.formatters import CustomJsonFormatter


class SanicJsonFormatter(CustomJsonFormatter):
    def __init__(self, *args):
        super(SanicJsonFormatter, self).__init__(*args,
                                                 json_indent=CONFIG.LOGGING.json_logger_indent,
                                                 coloured_logging=CONFIG.LOGGING.coloured_logging)

    def add_fields(self, log_record, record, message_dict):
        super(SanicJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['namespace'] = CONFIG.LOGGING.namespace
