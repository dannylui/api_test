import requests
import functools
import logging


def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        ret = func(*args, **kwargs)
        logging.info(f"Response: {ret[0]} {ret[1]}")
        return ret
    return wrapper_debug


class HttpConnector:
    def __init__(self, host, port=None, base_path=None, proto="https"):
        self._base_url = f"{proto}://{host}{':'+port if port else ''}{'/'+base_path if base_path else ''}"
        # set up common attributes shared between requests, such as creds/auth, headers, response handling, etc
        self._auth = None
        self._headers = None

    def http_func(self, func, sub_url, data=None):
        url = "/".join([self._base_url, sub_url])
        logging.info(f"Request: method={func.__name__} {url=} {data=}")
        response = func(url, json=data, headers=self._headers)
        return response.status_code, response.json()

    @debug
    def get(self, sub_url):
        return self.http_func(requests.get, sub_url)

    @debug
    def post(self, sub_url, data):
        return self.http_func(requests.post, sub_url, data)
