from http_connector.http_connector import HttpConnector
from config import config
import logging


class ClientBase:

    def __init__(self):
        self._http = HttpConnector(config['host'])
        self._resource = None

    def get(self, resource):
        status_code, response_json = self._http.get(resource)
        if status_code != 200:
            raise Exception('response code was not success')
        return response_json

    def get_collection(self):
        return self.get(self._resource)

    def get_item(self, post_id):
        return self.get(f"{self._resource}/{post_id}")

    def post(self, resource, data):
        status_code, response_json = self._http.post(resource, data)
        if status_code != 201:
            raise Exception('response code was not success')
        return response_json

    def create_item(self, data):
        return self.post(self._resource, data)
