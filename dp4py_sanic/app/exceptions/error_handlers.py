"""
Defines custom Sanic error handlers
"""
import logging
import sanic.exceptions

from sanic.response import json

from dp4py_sanic.app.server import Server
from dp4py_sanic.app.request import Request


class ErrorHandlers(object):

    @staticmethod
    def register(app: Server):
        # Explicitly handle RequestTimeouts -> These are logged out as Errors by default (unwanted)
        @app.exception(sanic.exceptions.RequestTimeout)
        def timeout(request: Request, exception: sanic.exceptions.SanicException):
            extra = {}
            if request is not None:
                extra["context"] = request.request_id

            logging.debug("RequestTimeout from error_handler.", exc_info=exception, extra=extra)
            return json({"message": "RequestTimeout from error_handler."}, exception.status_code)
