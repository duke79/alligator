from app import db
from sqlalchemy.dialects.mysql import INTEGER


class Category(db.Model):
    __tablename__ = 'category'
    title = db.Column(db.String(50), nullable=True, unique=True)
