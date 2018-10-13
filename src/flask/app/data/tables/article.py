from sqlalchemy import ForeignKey

from app import db
from sqlalchemy.dialects.mysql import INTEGER

from app.data.tables.channel import Channel


class Article(db.Model):
    __tablename__ = 'article'
    link = db.Column(db.String(760), nullable=True, unique=True,
                     comment="Keeping it unique, assuming same url may not serve two distinct feeds")
    title = db.Column(db.String(500), nullable=True)
    # language = db.Column(db.String(50), nullable=True) # Doesn't it depend on source channel?
    description = db.Column(db.Text(), nullable=True)
    image = db.Column(db.String(2013), nullable=True)
    author = db.Column(db.String(100), nullable=True)
    guid = db.Column(db.String(760), nullable=True, unique=True)
    pubDate = db.Column(db.TIMESTAMP(), nullable=True)
    source_channel_id = db.Column(INTEGER(unsigned=True), ForeignKey(Channel.id), nullable=True)
