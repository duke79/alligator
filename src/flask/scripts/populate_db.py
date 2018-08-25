from datetime import datetime
from time import mktime

import feedparser

from app.data.tables.article import Article
from app.graph.category.data import get_categories, add_category
from app.graph.channel.data import add_channel, get_channels
from app.utils import safeDict
from app.utils.feedly_client import FeedlyClient


def populate_categories_channels(populateChannels=False):
    feedly = FeedlyClient(
        client_id="sandbox",  # https://groups.google.com/forum/#!topic/feedly-cloud/9hUAAjulF30
        client_secret="LbQeeuE3YjcKwDBU",  # (expires on October 1st 2018)
        sandbox=True
    )

    for category in get_categories():
        res = feedly.search(category.title, 5).json()
        for result in safeDict(res, ["results"]):
            tags = safeDict(result, ["deliciousTags"])
            for tag in tags:
                add_category(tag)
            url = safeDict(result, ["feedId"])[5:]
            if populateChannels:
                channel = add_channel(url)
                # TODO: Get id of the newly added channel? To populate article right from here too?
                pass


def populate_articles():
    for channel in get_channels():
        channel_id = channel.id
        channel = feedparser.parse(channel.link)
        for entry in safeDict(channel, ["entries"]):
            image = None
            try:
                image = safeDict(entry, ["media_content"])
                if image:
                    if len(image) > 0:
                        image = safeDict(image[0], ["url"])
            except Exception as e:
                print(e)
            pubDate = None
            try:
                pubDate = safeDict(entry, ["published_parsed"]),
                if pubDate:
                    if len(pubDate) > 0:
                        tub_date = pubDate[0]
                        if len(tub_date) > 0:
                            pubDate = datetime.fromtimestamp(mktime(tub_date))
            except Exception as e:
                print(e)
            article = Article(source_channel_id=channel_id,
                              link=safeDict(entry, ["link"]),
                              title=safeDict(entry, ["title"]),
                              description=safeDict(entry, ["summary"]),
                              image=image,
                              guid=safeDict(entry, ["id"]),
                              pubDate=pubDate
                              )
            article.save()


if __name__ == "__main__":
    # populate_categories_channels(populateChannels=True)
    populate_articles()
