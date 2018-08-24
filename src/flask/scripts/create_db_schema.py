from app import db
from app.data.tables.category import Category
from app.data.tables.channel import Channel
from app.data.tables.user import User

if __name__ == "__main__":
    """ Dummy instantiation """
    category = Category()
    channel = Channel()
    user = User()

    """ Initialize schema in mysql database """
    db.create_all()
