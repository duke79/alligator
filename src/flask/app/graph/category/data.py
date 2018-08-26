from sqlalchemy.exc import DatabaseError

from app.data.mysql import MySQL
from app.data.tables.category import Category


def add_category(title):
    category = Category(title=title)
    try:
        return category.save()
    except DatabaseError as e:
        code = e.orig.args[0]
        if code == 1062:
            return Category.query.filter(Category.title==title).first()
        return None



def remove_category(id):
    res = Category.query.filter_by(id=id).first()
    res.delete()


def update_category(id, title):
    res = Category.query.filter_by(id=id).first()
    res.update(title=title)


def get_categories(ids=None, query=None, channel_id=None, limit=None):  # TODO : Add where clause, filters
    ret = Category.query
    if query:
        ret.filter(Category.title.ilike("%" + query + "%"))
    ret = ret.limit(limit)
    return ret
