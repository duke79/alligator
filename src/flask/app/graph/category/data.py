from app import db_session
from app.data.mysql import MySQL
from app.data.tables.category import Category


def add_category(title):
    # with MySQL() as mysql:
    #     try:
    #         cursor = mysql.insert("category", {
    #             "title": title,
    #         })
    #     except Exception as e:
    #         print(e)
    category = Category(title=title)
    db_session.add(category)
    db_session.commit()

def remove_category(id):
    with MySQL() as mysql:
        mysql.delete("category", id)
        


def update_category(id, title):
    with MySQL() as mysql:
        cursor = mysql.update("category", {
            "title": title,
        }, "`id`=%s" % id)


def get_categories(ids=None, query=None, channel_id=None, limit=None):  # TODO : Add where clause, filters
    # with MySQL() as mysql:
    #     cursor = mysql.execute("select * from `category`;")
    #     rows = cursor.fetchall()
    #     return rows
    ret = Category.query.all()
    return ret
