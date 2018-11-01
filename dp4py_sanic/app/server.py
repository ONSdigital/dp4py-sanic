"""
Defines a Sanic server class which uses the dp4py_logging library for JSON logging
"""
import logging

from sanic import Sanic
from sanic_prometheus import monitor

from dp4py_sanic.config import CONFIG
from dp4py_sanic.app.request import Request
from dp4py_sanic.app.exceptions.error_handlers import ErrorHandlers
from dp4py_sanic.logging.log_config import log_config as sanic_log_config


class Server(Sanic):
    def __init__(self, name=None, router=None, error_handler=None,
                 load_env=True, request_class=Request,
                 strict_slashes=False, log_config=sanic_log_config,
                 configure_logging=True):
        super(Server, self).__init__(name=name, router=router, error_handler=error_handler,
                                     load_env=load_env, request_class=request_class,
                                     strict_slashes=strict_slashes, log_config=log_config,
                                     configure_logging=configure_logging)

        # Enable prometheus metrics?
        if CONFIG.APP.prometheus_metrics_enabled:
            logging.info("Prometheus metrics enabled: Enabling /metrics endpoint.")
            monitor(self).expose_endpoint()
