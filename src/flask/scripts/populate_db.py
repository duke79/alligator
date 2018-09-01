from datetime import datetime
from time import mktime

import feedparser
from sqlalchemy.exc import DatabaseError

from app.data.tables.article import Article
from app.graph.category.data import get_categories, add_category
from app.graph.channel.data import add_channel, get_channels
from app.utils import safeDict
from app.utils.feedly_client import FeedlyClient
from app.utils.traces import print_exception_traces


def populate_articles_from_channel(channel):
    if not channel:
        return
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
        try:
            article.save()
        except DatabaseError as e:
            print_exception_traces(e)


def populate_articles():
    for channel in get_channels():
        populate_articles_from_channel(channel)


def populate_categories(channels_per_category=5,
                        withChannels=False,
                        withArticles=False):
    feedly = FeedlyClient(
        client_id="sandbox",  # https://groups.google.com/forum/#!topic/feedly-cloud/9hUAAjulF30
        client_secret="LbQeeuE3YjcKwDBU",  # (expires on October 1st 2018)
        sandbox=True
    )

    categories = get_categories()
    for counter, category in enumerate(categories):
        res = feedly.search(category.title, channels_per_category).json()
        for result in safeDict(res, ["results"]):
            tags = safeDict(result, ["deliciousTags"])
            categories = []
            for tag in tags:
                category = add_category(tag)
                if category:
                    categories.append(category.id)
            url = safeDict(result, ["feedId"])[5:]
            if withChannels or withArticles:
                channel = add_channel(url, categories=categories)
                if withArticles and channel:
                    populate_articles_from_channel(channel)


if __name__ == "__main__":
    populate_categories(withChannels=True,
                        withArticles=False,
                        channels_per_category=1)
    # populate_articles()
