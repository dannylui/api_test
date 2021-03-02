from api_client.posts import Posts
from config import config
import logging


if config.debug:
  logging.basicConfig(level=logging.INFO)

logging.info(f"{config=}")

posts = Posts()
# posts.get_posts()
posts.get_post(1)
posts.add_post(
    {
        "title": "foo",
        "body": "bar",
        "userId": 1,
    }
)
