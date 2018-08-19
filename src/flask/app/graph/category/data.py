import feedparser

from app.data.config import Config
from app.data.mysql import MySQL
from app.utils import safeDict


def add_category(title):
    with MySQL() as mysql:
        cursor = mysql.insert("category", {
            "title": title,
        })


def remove_category(id):
    with MySQL() as mysql:
        mysql.delete("category", id)


def update_category(id, title):
    with MySQL() as mysql:
        cursor = mysql.update("category", {
            "title": title,
        }, "`id`=%s" % id)


def get_categories(ids=None, query=None, channel_id=None, limit=None):  # TODO : Add where clause, filters
    with MySQL() as mysql:
        cursor = mysql.execute("select * from `category`;")
        rows = cursor.fetchall()
        return rows
