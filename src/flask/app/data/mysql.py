import pymysql
from app.data.config import Config


class MySQLError(Exception):
    pass


class MySQL():
    def __init__(self):
        self.config = Config()["database"]["mysql"]

        # Queries
        self.QUERY_CREATE_USER = "create user 'vilokanlabs'@'localhost' identified by '%s';" % (self.config["password"])
        self.QUERY_GRANT_PERMISSION = "grant all privileges on yojaka.* to 'vilokanlabs'@'localhost' with grant option;"
        self.QUERY_CREATE_DB = "CREATE DATABASE `yojaka`;"
        self.QUERY_CHANGE_DB = "use yojaka;"
        self.QUERY_CREATE_USER_TABLE = """
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
        self.QUERY_SELECT_USERS_ALL = "select * from user;"
        self.QUERY_SELECT_USERS_10 = "select * from user limit 10;"
        self.QUERY_SELECT_USER_BY_FIREBASE_ID = "select * from user where `firebase_uid`='%s';"
        self.QUERY_SELECT_ALL_TABLES = """select table_name from information_schema.tables where table_type="BASE TABLE" and table_schema="yojaka";"""
        self.QUERY_INSERT_USER = """INSERT INTO `user` (`name`, `phone_number`, `photo_url`, `email`, `firebase_uid`) VALUES ('%s', '%s', '%s', '%s', '%s');"""
        self.QUERY_UPDATE_USER_NAME = """UPDATE `user` SET `name`='%s' WHERE `id`=%s;"""
        self.QUERY_UPDATE_USER_PHONE_NUMBER = """UPDATE `user` SET `phone_number`='%s' WHERE `id`=%s;"""
        self.QUERY_UPDATE_USER_PHOTO_URL = """UPDATE `user` SET `photo_url`='%s' WHERE `id`=%s;"""
        self.QUERY_UPDATE_USER_EMAIL = """UPDATE `user` SET `email`='%s' WHERE `id`=%s;"""
        self.QUERY_UPDATE_USER_FIREBASE_UID = """UPDATE `user` SET `firebase_uid`='%s' WHERE `id`=%s;"""

        # Connect to the host
        self.conn = pymysql.connect(host=self.config["host"],
                                    user=self.config["user"],
                                    password=self.config["password"])

        # SSDict avoids caching rows in python | https://stackoverflow.com/q/17861152/973425
        self.cursor = self.conn.cursor(pymysql.cursors.SSDictCursor)

        # Switch to the database
        self.cursor.execute(self.QUERY_CHANGE_DB)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()

    def execute(self, query):
        try:
            cursor = self.cursor.execute(query)
            pass
        except Exception as e:
            raise e
        return self.cursor

    def commit(self):
        self.conn.commit()

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
            self.execute(self.QUERY_INSERT_USER % (name, phone, photo, email, firebase_uid))
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
            query = self.QUERY_UPDATE_USER_NAME % (name, mysql_user['id'])
            res = self.execute(query)
            query = self.QUERY_UPDATE_USER_PHONE_NUMBER % (phone, mysql_user['id'])
            res = self.execute(query)
            query = self.QUERY_UPDATE_USER_PHOTO_URL % (photo, mysql_user['id'])
            res = self.execute(query)
            query = self.QUERY_UPDATE_USER_EMAIL % (email, mysql_user['id'])
            res = self.execute(query)
            query = self.QUERY_UPDATE_USER_FIREBASE_UID % (firebase_uid, mysql_user['id'])
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

        cursor = self.execute(self.QUERY_SELECT_USER_BY_FIREBASE_ID % (uid))
        return cursor.fetchone()


if __name__ == "__main__":
    with MySQL() as mysql:
        mysql.import_all_firebase_users()
        mysql_users = mysql.execute("select * from user;")
        for user in mysql_users:
            print(user)
            pass
