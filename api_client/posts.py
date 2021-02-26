from api_client.client_base import ClientBase

class Posts(ClientBase):

    def __init__(self):
        super().__init__()
        self._resource = 'posts'

    # def get_posts(self):
    #     status_code, response_json = self._http_conn.get(self._resource)
    #     if status_code != 200:
    #         raise Exception('response code was not success')
    #     return response_json

    # def get_post(self, post_id):
    #     status_code, response_json = self._http_conn.get(f"{self._resource}/{post_id}")
    #     if status_code != 200:
    #         raise Exception('response code was not success')
    #     return response_json


    def get_posts(self):
        return self.get_collection()

    def get_post(self, post_id):
        return self.get_item(post_id)

    def add_post(self, data):
        return self.create_item(data)
        