import feedparser

from app.data.config import Config
from app.data.firebase import Firebase
from app.data.mysql import MySQL
from app.utils.singleton import Singleton

config = Config()


class DB(metaclass=Singleton):
    def __init__(self):
        try:
            self.firebase = Firebase()
        except FileNotFoundError as e:  # If serviceAccountKey is not provided
            raise e
        self.mysql = MySQL()
        self.session = dict()

    def init_session(self, session_id):
        """Authentication helper to retrieve the firebase user info from firebase session id"""
        try:
            uid = self.firebase.get_user_uid_from_session(session_id)
            self.session["firebase_session_id"] = session_id
            self.session["firebase_uid"] = uid
            db_user = self.get_user_by_uid(uid, reimport=True)  # Firebase sync enabled in every
            if not db_user:
                raise Exception("User doesn't exist in local database")
            self.session["current_user"] = db_user
            return self.session
        except Exception as e:
            # return str(e), 400  # 400 = Bad Request
            return None

    def get_user_by_uid(self, uid, reimport=False):
        """
        Get user by uid
        :param uid:
        :param reimport: Sync database user from firebase user
        :return:
        """
        user = self.mysql.get_user_by_firebase_uid(uid, reimport=reimport)
        return user

    def get_users_all(self, prefix=""):
        cursor = self.mysql.execute("select id from user;")
        users = cursor.fetchall()
        return users

    def get_user_by_id(self, id):
        cursor = self.mysql.execute("select * from user where id='%s';" % (id))
        user = cursor.fetchone()
        return user

    def check_permission(self, permission_bit, user_id=None):
        """
        :param permission_bit:
        :param user_id: defaults to current user in 'self.session'
        :return: Returns True if queried permissions exist for the user
        """
        ret = False
        try:
            user_id = self.session["current_user"]["id"]
            cursor = self.mysql.execute(
                "select * from permission where permission_bit='%s' and user_id='%s'"
                % (permission_bit, user_id)
            )
            permission = cursor.fetchone()
            if permission:
                ret = True
        except Exception as e:
            pass

        if config["debug"]:
            ret = True

        return ret

    def get_feed_by_id(self, feed_id):
        return {
            "title": "This is the title of the feed",
            "picture": "https://news.sky.com/assets/2018/sky-news-logo.png",
            "detail": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        }

