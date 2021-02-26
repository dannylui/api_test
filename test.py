import logging
logging.basicConfig(level=logging.INFO)

from api_client.posts import Posts
from config import config


posts = Posts()
posts.get_posts()
posts.get_post(1)
posts.add_post(
    {
        "title": "foo",
        "body": "bar",
        "userId": 1,
    }
)
