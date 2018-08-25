from sqlalchemy import ForeignKey

from app import db
from sqlalchemy.dialects.mysql import INTEGER


class ChannelCategories(db.Model):
    __tablename__ = 'channel_categories'
    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True, nullable=False)
    category_id = db.Column(INTEGER(unsigned=True), ForeignKey("category.id"), nullable=False)
    channel_id = db.Column(INTEGER(unsigned=True), ForeignKey("channel.id"), nullable=False)
    created_at = db.Column(db.TIMESTAMP(), nullable=False,
                           server_default=db.text('CURRENT_TIMESTAMP'))
    updated_at = db.Column(db.TIMESTAMP(), nullable=False,
                           server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                           )
