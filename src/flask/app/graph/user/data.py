import feedparser
from sqlalchemy.exc import DatabaseError

from app.data.config import Config
from app.data.mysql import MySQL
from app.data.tables.category import Category
from app.data.tables.user_categories import UserCategories
from app.utils import safeDict
from app.utils.traces import print_exception_traces


def add_user_categories(user_id, category_ids):
    for category_id in category_ids:
        user_category = UserCategories(user_id=user_id,
                                       category_id=category_id)
        try:
            user_category.save()
        except DatabaseError as e:
            print_exception_traces(e)


def remove_user_categories(user_id, category_ids):
    for category_id in category_ids:
        user_category = UserCategories.query.filter(UserCategories.user_id == user_id) \
            .filter(UserCategories.category_id == category_id).first()
        if user_category:
            user_category.delete()


def update_user_categories(user_id, category_ids):
    user_categories = UserCategories.query.filter(user_id == user_id).all()
    for category in user_categories:
        category_id = category.category_id
        user_category = UserCategories.query.filter(UserCategories.user_id == user_id) \
            .filter(UserCategories.category_id == category_id).first()
        if user_category:
            user_category.delete()
    add_user_categories(user_id, category_ids)


def get_user_categories(user_id, category_ids=None, query=None, channel_id=None, limit=None):  # TODO : Handle filters
    user_categories = UserCategories.session().query(Category).join(UserCategories)
    user_categories = user_categories.filter(UserCategories.user_id == user_id)
    user_categories = user_categories.limit(limit)
    return user_categories
