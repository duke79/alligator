from app import db
from app.data.tables import *

if __name__ == "__main__":
    """ Dummy instantiation """
    # category = Category()
    # channel = Channel()
    # user = User()

    """ Initialize schema in mysql database """
    db.create_all()
