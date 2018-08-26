import feedparser
from sqlalchemy.exc import DatabaseError

from app.data.config import Config
from app.data.mysql import MySQL
from app.data.tables.article import Article
from app.data.tables.category import Category
from app.data.tables.user import User
from app.data.tables.user_categories import UserCategories
from app.graph.user.actions_feed import SortField
from app.graph.user.data_categories import get_user_categories
from app.utils import safeDict
from app.utils.traces import print_exception_traces


def get_user_feed(user_id, sort_by=None, sort_order=None, limit=None):
    user_feed = Article.session().query(Article)
    if sort_by:
        for counter, sort_field in enumerate(sort_by):
            order_by = None
            if sort_field == SortField.UPDATED_DATE:
                order_by = Article.updated_at
            if sort_field == SortField.PUBLISHED_DATE:
                order_by = Article.pubDate
            if sort_field == SortField.CATEGORY:
                pass  # TODO

            if order_by:
                if sort_order:
                    if not sort_order[counter]:
                        order_by = order_by.desc()
                user_feed = user_feed.order_by(order_by)
    # user_categories = user_categories.join(UserCategories)
    # user_categories = user_categories.filter(UserCategories.user_id == user_id)
    user_feed = user_feed.limit(limit)

    return user_feed
