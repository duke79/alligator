import feedparser

from app.data.config import Config
from app.data.mysql import MySQL
from app.utils import safeDict


def add_user_categories(user_id, category_ids):
    with MySQL() as mysql:
        for category_id in category_ids:
            cursor = mysql.insert("user_categories", {
                "user_id": user_id,
                "category_id": category_id
            })
        pass


def remove_user_categories(user_id, category_ids):
    with MySQL() as mysql:
        for category_id in category_ids:
            cursor = mysql.delete("user_categories", "user_id={0} and category_id={1}".format(user_id, category_id))
        pass


def update_user_categories(user_id, category_ids):
    with MySQL() as mysql:
        # 0. Begin SQL transaction
        mysql.execute("BEGIN;")
        # 1. Delete existing user categories
        cursor = mysql.delete("user_categories", "user_id={0}".format(user_id))
        # 2. Insert new categories
        for category_id in category_ids:
            cursor = mysql.insert("user_categories", {
                "user_id": user_id,
                "category_id": category_id
            })
        mysql.execute("COMMIT;")


def get_user_categories(user_id, category_ids=None, query=None, channel_id=None, limit=None):  # TODO : Handle filters
    with MySQL() as mysql:
        cursor = mysql.execute(
            "select `category`.`*` from `user_categories` "
            "inner join `category` on `user_categories`.`category_id`=`category`.`id` "
            "where `user_id`={0};".format(user_id))
        rows = cursor.fetchall()
        return rows
