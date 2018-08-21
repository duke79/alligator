import feedparser

from app.data.config import Config
from app.data.mysql import MySQL
from app.utils import safeDict


def add_channel(url, categories=None):  # TODO : Handle categories
    with MySQL() as mysql:
        try:
            channel = feedparser.parse(url)
            title = safeDict(channel, ["feed", "title"])
            language = safeDict(channel, ["feed", "language"])
            image = safeDict(channel, ["feed", "image", "href"])
            description = safeDict(channel, ["feed", "subtitle"])
            copyright = safeDict(channel, ["feed", "rights_detail", "value"])
            # query = "INSERT INTO `channel` (`link`, `title`, `language`, `description`, `image`, `copyright`) " \
            #         "VALUES (`%s`,`%s`,`%s`,`%s`,`%s`,`%s`);" \
            #         % (url, title, language, description, image, copyright)
            # cursor = mysql.execute(query)
            cursor = mysql.insert("channel", {
                "link": url,
                "title": title,
                "language": language,
                "description": description,
                "image": image,
                "copyright": r"%s" % copyright
            })
            pass
        except Exception as e:
            print(e)


def remove_channel(id):
    with MySQL() as mysql:
        cursor = mysql.delete("channel", "`id`={0}".format(id))
        pass


def update_channel(id, url=None, categories=None):  # TODO : Handle categories
    with MySQL() as mysql:
        channel = feedparser.parse(url)
        title = safeDict(channel, ["feed", "title"])
        language = safeDict(channel, ["feed", "language"])
        image = safeDict(channel, ["feed", "image", "href"])
        description = safeDict(channel, ["feed", "subtitle"])
        copyright = safeDict(channel, ["feed", "rights_detail", "value"])
        cursor = mysql.update("channel", {
            "link": url,
            "title": title,
            "language": language,
            "description": description,
            "image": image,
            "copyright": r"%s" % copyright
        }, "`id`=%s" % id)
        pass


def get_channels(ids=None, category_id=None, match_in_url=None, limit=None):  # TODO : Add where clause, filters
    # channels = []
    # config = Config()
    # urls = config["rss_sources"]
    # for url in urls:
    #     channel = feedparser.parse(url)
    #     channels.append(channel)
    #     return channels
    with MySQL() as mysql:
        cursor = mysql.execute("select * from `channel`;")
        rows = cursor.fetchall()
        return rows
