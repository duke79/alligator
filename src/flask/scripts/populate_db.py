from app.graph.category.data import get_categories, add_category
from app.graph.channel.data import add_channel
from app.utils import safeDict
from app.utils.feedly_client import FeedlyClient


def populate_categories_channels(populateChannels=False):
    feedly = FeedlyClient(
        client_id="sandbox",  # https://groups.google.com/forum/#!topic/feedly-cloud/9hUAAjulF30
        client_secret="LbQeeuE3YjcKwDBU",  # (expires on October 1st 2018)
        sandbox=True
    )

    for category in get_categories():
        res = feedly.search(safeDict(category, ["title"]), 5).json()
        for result in safeDict(res, ["results"]):
            tags = safeDict(result, ["deliciousTags"])
            for tag in tags:
                add_category(tag)
            url = safeDict(result, ["feedId"])[5:]
            if populateChannels:
                add_channel(url)


if __name__ == "__main__":
    populate_categories_channels(populateChannels=True)
