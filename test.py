# from api_client.http_connector import Http_Connector
import logging
logging.basicConfig(level=logging.INFO)
from config import config

# print(config)

# http_connector = Http_Connector(config['host'])
# http_connector.get('posts/1')
# http_connector.post('posts', {
#     'title': 'foo',
#     'body': 'bar',
#     'userId': 1,
#   })

from api_client.posts import Posts

posts = Posts()
posts.get_posts()
posts.get_post(1)
posts.add_post({
    'title': 'foo',
    'body': 'bar',
    'userId': 1,
  })