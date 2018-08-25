from app import db
from sqlalchemy.dialects.mysql import INTEGER


class Channel(db.Model):
    __tablename__ = 'channel'
    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True, nullable=False)
    link = db.Column(db.String(760), nullable=True, unique=True,
                     comment="Keeping it unique, assuming same url may not serve two distinct feeds")
    title = db.Column(db.String(500), nullable=True)
    language = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(500), nullable=True)
    image = db.Column(db.String(2013), nullable=True)
    copyright = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.TIMESTAMP(), nullable=False,
                           server_default=db.text('CURRENT_TIMESTAMP'))
    updated_at = db.Column(db.TIMESTAMP(), nullable=False,
                           server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                           )
