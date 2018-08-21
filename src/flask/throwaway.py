from app.graph.category.data import get_categories, add_category
from app.graph.channel.data import add_channel
from app.utils.feedly_client import FeedlyClient

feedly = FeedlyClient(
    client_id="sandbox",  # https://groups.google.com/forum/#!topic/feedly-cloud/9hUAAjulF30
    client_secret="LbQeeuE3YjcKwDBU",  # (expires on October 1st 2018)
    sandbox=True
)

for category in get_categories():
    res = feedly.search(category["title"], 5).json()
    for result in res["results"]:
        tags = result["deliciousTags"]
        for tag in tags:
            add_category(tag)
        url = result["feedId"][5:]
        add_channel(url)
        pass
