from sqlalchemy import ForeignKey, UniqueConstraint

from app import db
from sqlalchemy.dialects.mysql import INTEGER

from app.data.tables.category import Category
from app.data.tables.channel import Channel


class ChannelCategories(db.Model):
    __tablename__ = 'channel_categories'
    category_id = db.Column(INTEGER(unsigned=True), ForeignKey(Category.id), nullable=False)
    channel_id = db.Column(INTEGER(unsigned=True), ForeignKey(Channel.id), nullable=False)
    __table_args__ = (UniqueConstraint('category_id', 'channel_id', name='channel_category'),)
