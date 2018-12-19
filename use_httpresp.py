# -*- coding: utf-8 -*-


import json

from requests.models import Response, Request
from urllib3 import HTTPResponse
from io import BytesIO

if __name__ == '__main__':
    fake_resp = json.dumps({'msg': 'success'})

    body = BytesIO(fake_resp)

    request = Request(method='POST', url='/hello')

    resp = HTTPResponse(body=body,
                        status=200,
                        preload_content=False,
                        headers={'content-type': 'application/json'}
                        )

    # cannot inst with params, should change the instance after insting
    response = Response()

    response.status_code = resp.status

    response.raw = resp
    response.reason = response.raw.reason

    response.url = request.url

    response.request = request
    print response.content
