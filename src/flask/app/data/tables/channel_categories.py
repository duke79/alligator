from sqlalchemy import ForeignKey, UniqueConstraint

from app import db
from sqlalchemy.dialects.mysql import INTEGER

from app.data.tables.category import Category
from app.data.tables.channel import Channel


class ChannelCategories(db.Model):
    __tablename__ = 'channel_categories'
    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True, nullable=False)
    category_id = db.Column(INTEGER(unsigned=True), ForeignKey(Category.id), nullable=False)
    channel_id = db.Column(INTEGER(unsigned=True), ForeignKey(Channel.id), nullable=False)
    created_at = db.Column(db.TIMESTAMP(), nullable=False,
                           server_default=db.text('CURRENT_TIMESTAMP'))
    updated_at = db.Column(db.TIMESTAMP(), nullable=False,
                           server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    __table_args__ = (UniqueConstraint('category_id', 'channel_id', name='channel_category'),
                      )
