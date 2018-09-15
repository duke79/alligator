from math import ceil

import feedparser
from sqlalchemy import func
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


def get_user_feed(user_id, sort_by=None, sort_order=None, limit=10, offset=0):  # TODO: Sort again! :(
    nbr_user_categories = UserCategories.session().query(func.count(UserCategories.id)).filter(
        UserCategories.user_id == user_id).scalar()
    limit_per_category = ceil(limit / nbr_user_categories)
    query = """
        select * from
        (
        select article.id, 
            article.link, 
            article.title as title, 
            article.description as description,
            article.image as media_content, 
            channel.id as channel, 
            category.title as category, 
            row_number() over (partition by category.title) as r from article 
        inner join channel on article.source_channel_id=channel.id 
        inner join channel_categories on channel_categories.channel_id=channel.id 
        inner join category on channel_categories.category_id=category.id
        inner join user_categories on user_categories.category_id=category.id
        inner join user on user_categories.user_id=user.id
        where category.id in (select category.id from category inner join user_categories on user_categories.category_id=category.id where user_categories.user_id={0} order by category.title desc)
        #where category.id=19
        group by article.id
        order by article.id desc, category.title desc
        ) as main
        where main.r <= {1} limit {2} offset {3} 
        """.format(user_id, limit_per_category, limit, offset)

    with MySQL() as mysql:
        user_feed = mysql.execute(query).fetchall()
        return user_feed
