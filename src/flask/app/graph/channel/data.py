import feedparser
from sqlalchemy.exc import DatabaseError

from app import db_session
from app.data.config import Config
from app.data.mysql import MySQL
from app.data.tables.article import Article
from app.data.tables.channel import Channel
from app.utils import safeDict


def add_channel(url, categories=None):  # TODO : Handle categories
    channel = feedparser.parse(url)
    title = safeDict(channel, ["feed", "title"])
    language = safeDict(channel, ["feed", "language"])
    image = safeDict(channel, ["feed", "image", "href"])
    description = safeDict(channel, ["feed", "subtitle"])
    copyright = safeDict(channel, ["feed", "rights_detail", "value"])
    copyright = r"%s" % copyright
    channel = Channel(link=url,
                      title=title,
                      language=language,
                      image=image,
                      description=description,
                      copyright=copyright)
    return channel.save()


def remove_channel(id):
    res = Channel.query.filter_by(id=id).first()
    res.delete()


def update_channel(id, url=None, categories=None):  # TODO : Handle categories
    channel = feedparser.parse(url)
    title = safeDict(channel, ["feed", "title"])
    language = safeDict(channel, ["feed", "language"])
    image = safeDict(channel, ["feed", "image", "href"])
    description = safeDict(channel, ["feed", "subtitle"])
    copyright = safeDict(channel, ["feed", "rights_detail", "value"])
    copyright = r"%s" % copyright
    res = Channel.query.filter_by(id=id).first()
    res.update(link=url,
               title=title,
               language=language,
               image=image,
               description=description,
               copyright=copyright)


def get_channels(ids=None, category_id=None, match_in_url=None, limit=None):  # TODO : Add where clause, filters
    """
    Ref: https://stackoverflow.com/questions/3332991/sqlalchemy-filter-multiple-columns
    :param ids:
    :param category_id:
    :param match_in_url:
    :param limit:
    :return:
    """
    ret = Channel.query
    if match_in_url:
        ret = ret.filter(Channel.link.like("%" + match_in_url + "%"))
    ret = ret.limit(limit)
    return ret
