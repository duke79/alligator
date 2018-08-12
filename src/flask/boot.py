import os

# Generate queries for to : Create user and grant permissions
os.environ["boot"] = "1"  # To be used to boot mysql
from app.data.mysql import MySQL
# with MySQL() as mysql:
#     pass
