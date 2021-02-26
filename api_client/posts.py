from api_client.client_base import ClientBase


class Posts(ClientBase):
    def __init__(self):
        super().__init__()
        self._resource = "posts"

    def get_posts(self):
        return self.get_collection()

    def get_post(self, post_id):
        return self.get_item(post_id)

    def add_post(self, data):
        return self.create_item(data)
