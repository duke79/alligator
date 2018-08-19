import os

import pymysql
from app.data.config import Config

config = Config()["database"]["mysql"]


class MySQLError(Exception):
    pass


class MySQLQuery():
    CREATE_USER = "create user '%s'@'%s' identified by '%s';" \
                  % (config["user"], config["host"], config["password"])
    GRANT_PERMISSION = "grant all privileges on %s.* to '%s'@'%s' with grant option;" \
                       % (config["db"], config["user"], config["host"])
    CREATE_DB = "CREATE DATABASE `%s`;" % (config["db"])
    CHANGE_DB = "use %s;" % (config["db"])
    CREATE_USER_TABLE = """
                CREATE TABLE `user` (
                `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
                `name` VARCHAR(200) NULL DEFAULT NULL,
                `phone_number` VARCHAR(50) NULL DEFAULT NULL,
                `photo_url` VARCHAR(2013) NULL DEFAULT NULL,
                `email` VARCHAR(200) NULL DEFAULT NULL,
                `firebase_uid` VARCHAR(100) NULL DEFAULT NULL,
                PRIMARY KEY (`id`)
                )
                COLLATE='utf8mb4_0900_ai_ci'
                ENGINE=InnoDB
                ;
                """
    SELECT_USERS_ALL = "select * from user;"
    SELECT_USERS_10 = "select * from user limit 10;"
    SELECT_USER_BY_FIREBASE_ID = "select * from user where `firebase_uid`='%s';"
    SELECT_ALL_TABLES = """select table_name from information_schema.tables where table_type="BASE TABLE" and table_schema="%s";""" % (
        config["db"])
    INSERT_USER = """INSERT INTO `user` (`name`, `phone_number`, `photo_url`, `email`, `firebase_uid`) VALUES ('%s', '%s', '%s', '%s', '%s');"""
    UPDATE_USER_NAME = """UPDATE `user` SET `name`='%s' WHERE `id`=%s;"""
    UPDATE_USER_PHONE_NUMBER = """UPDATE `user` SET `phone_number`='%s' WHERE `id`=%s;"""
    UPDATE_USER_PHOTO_URL = """UPDATE `user` SET `photo_url`='%s' WHERE `id`=%s;"""
    UPDATE_USER_EMAIL = """UPDATE `user` SET `email`='%s' WHERE `id`=%s;"""
    UPDATE_USER_FIREBASE_UID = """UPDATE `user` SET `firebase_uid`='%s' WHERE `id`=%s;"""


class MySQL():
    def __init__(self):
        """
        :param boot: To enable first time booting (db creation, user privileges etc.)
        """

        # Queries
        self.query = MySQLQuery()

        # Connect to the host
        self.conn = pymysql.connect(host=config["host"],
                                    user=config["user"],
                                    password=config["password"])

        # SSDict avoids caching rows in python | https://stackoverflow.com/q/17861152/973425
        self.cursor = self.conn.cursor(pymysql.cursors.SSDictCursor)

        try:
            if os.environ["boot"] == "1":
                os.environ["boot"] = ""
                # schema_file = os.path.join(os.path.dirname(os.path.normpath(__file__)), "mysql_db_schema.sql")
                # f = open(schema_file)
                # query_schema = f.read()
                print(self.query.CREATE_USER)
                print(self.query.GRANT_PERMISSION)
                # self.cursor.execute(self.query.CREATE_USER)
                # self.cursor.execute(self.query.GRANT_PERMISSION)
                return
        except KeyError as e:
            pass

        # Switch to the database
        self.cursor.execute(self.query.CHANGE_DB)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.close()

    def execute(self, query):
        try:
            cursor = self.cursor.execute(query)
            pass
        except Exception as e:
            raise e
        return self.cursor

    def insert(self, table, row):
        """Ref: https://stackoverflow.com/questions/11363335/how-can-i-escape-the-input-to-a-mysql-db-in-python3"""
        try:
            cols = ', '.join('`{}`'.format(col) for col in row.keys())
            vals = ', '.join('%({})s'.format(col) for col in row.keys())
            sql = 'INSERT INTO `{0}` ({1}) VALUES ({2})'.format(table, cols, vals)
            self.cursor.execute(sql, row)
        except Exception as e:
            raise e
        return self.cursor

    def update(self, table, row, where):
        """Ref: https://stackoverflow.com/questions/11363335/how-can-i-escape-the-input-to-a-mysql-db-in-python3"""
        try:
            values = ', '.join('`{0}`="{1}"'.format(key, value) for key, value in row.items())
            sql = 'UPDATE `{0}` SET {1} WHERE {2}'.format(table, values, where)
            self.cursor.execute(sql)
        except Exception as e:
            raise e
        return self.cursor

    def delete(self, table, where):
        try:
            sql = "DELETE FROM `{0}` WHERE  {1};".format(table, where)
            self.cursor.execute(sql)
        except Exception as e:
            raise e
        return self.cursor

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    def import_one_firebase_user(self, user, reimport=False):
        """" A user is imported only if it doesn't already exist in mysql """
        ret = 0
        name = user.display_name
        phone = user.phone_number
        photo = user.photo_url
        email = user.email
        firebase_uid = user.uid
        cursor = self.execute("""select * from user where `firebase_uid`='%s';""" % (firebase_uid))
        rows = cursor.fetchall()
        if len(rows) < 1:
            self.execute(self.query.INSERT_USER % (name, phone, photo, email, firebase_uid))
            ret += 1
        elif reimport:
            mysql_user = rows[0]
            # if not name:
            #     name = ''
            # if not phone:
            #     phone = ''
            # if not photo:
            #     photo = ''
            # if not email:
            #     email = ''
            if not firebase_uid:
                raise MySQLError("firebase UID not valid")

            # phone, photo, email, firebase_uid,
            query = self.query.UPDATE_USER_NAME % (name, mysql_user['id'])
            res = self.execute(query)
            query = self.query.UPDATE_USER_PHONE_NUMBER % (phone, mysql_user['id'])
            res = self.execute(query)
            query = self.query.UPDATE_USER_PHOTO_URL % (photo, mysql_user['id'])
            res = self.execute(query)
            query = self.query.UPDATE_USER_EMAIL % (email, mysql_user['id'])
            res = self.execute(query)
            query = self.query.UPDATE_USER_FIREBASE_UID % (firebase_uid, mysql_user['id'])
            res = self.execute(query)
            # print(str(res._result.message, "utf-8"))
            ret += 1
        return ret

    def import_all_firebase_users(self, reimport=False):
        """" A user is imported only if it doesn't already exist in mysql """
        from app.data.firebase import Firebase
        ret = 0
        firebase = Firebase()
        firebase_users = firebase.getUsers()
        for user in firebase_users:
            ret += self.import_one_firebase_user(user, reimport=reimport)
        return ret

    def get_user_by_firebase_uid(self, uid, reimport=False):
        """
        Get user by firebase uid
        :param uid:
        :param reimport: Sync database user from firebase user
        :return:
        """
        from app.data.firebase import Firebase
        firebase = Firebase()

        fireabse_user = firebase.getUserByUID(uid)
        res = self.import_one_firebase_user(fireabse_user, reimport=reimport)

        cursor = self.execute(self.query.SELECT_USER_BY_FIREBASE_ID % (uid))
        return cursor.fetchone()


if __name__ == "__main__":
    with MySQL() as mysql:
        mysql.import_all_firebase_users()
        mysql_users = mysql.execute("select * from user;")
        for user in mysql_users:
            print(user)
            pass
