from app.data.mysql import MySQL
from app.data.tables.category import Category


def add_category(title):
    category = Category(title=title)
    category.save()



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
