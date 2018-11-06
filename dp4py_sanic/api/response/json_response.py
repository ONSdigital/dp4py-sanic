"""
Defines a wrapper fn for a json response which sets the X-Request-Id header
"""
from sanic.response import HTTPResponse, json_dumps

from dp4py_sanic.app.request import Request


def json(request: Request, body, status=200, headers: dict=None, dumps=json_dumps, **kwargs):
    """
    Returns response object with body in json format.
    :param request: The inbound request object.
    :param body: Response data to be serialized.
    :param status: Response code.
    :param headers: Custom Headers.
    :param kwargs: Remaining arguments that are passed to the json encoder.
    """
    content_type = "application/json"

    # Build headers
    if headers is None:
        headers = {}
    if Request.request_id_header not in headers:
        headers[Request.request_id_header] = request.request_id

    return HTTPResponse(dumps(body, **kwargs), headers=headers,
                        status=status, content_type=content_type)
