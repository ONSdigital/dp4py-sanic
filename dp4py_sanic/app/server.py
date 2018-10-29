"""
Defines a Sanic server class which uses the dp4py_logging library for JSON logging
"""
from sanic import Sanic

from dp4py_sanic.logging.log_config import log_config


class Server(Sanic):
    def __init__(self, name=None, router=None, error_handler=None,
                 load_env=True, request_class=None,
                 strict_slashes=False, log_config=log_config,
                 configure_logging=True):
        super(Server, self).__init__(name=name, router=router, error_handler=error_handler,
                                     load_env=load_env, request_class=request_class,
                                     strict_slashes=strict_slashes, log_config=log_config,
                                     configure_logging=configure_logging)
