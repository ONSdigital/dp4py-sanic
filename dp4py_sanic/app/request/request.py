"""
Wraps the Sanic request and adds request context
"""
from sanic import request
from uuid import uuid4


class Request(request.Request):
    request_id_header = "X-Request-Id"

    def __init__(self, *args, **kwargs):
        """
        Initialise the request object with a unique ID (either supplied as a header or generated)
        :param args:
        :param kwargs:
        """
        super(Request, self).__init__(*args, **kwargs)

        # Init empty request ID
        self.request_id = None

        # Check for existing ID
        if self.request_id_header in self.headers:
            self.request_id = self.headers.get(self.request_id_header)
        else:
            # Generate a random uuid4
            self.request_id = str(uuid4())
