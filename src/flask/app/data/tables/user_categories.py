from sqlalchemy import ForeignKey, UniqueConstraint

from app import db
from sqlalchemy.dialects.mysql import INTEGER

from app.data.tables.category import Category
from app.data.tables.user import User


class UserCategories(db.Model):
    __tablename__ = 'user_categories'
    user_id = db.Column(INTEGER(unsigned=True), ForeignKey(User.id), nullable=False)
    category_id = db.Column(INTEGER(unsigned=True), ForeignKey(Category.id), nullable=False)
    created_at = db.Column(db.TIMESTAMP(), nullable=False,
                           server_default=db.text('CURRENT_TIMESTAMP'))
