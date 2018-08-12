import firebase_admin
from firebase_admin import credentials, db, auth

from app.data.config import Config
from app.utils.singleton import Singleton


class Firebase(metaclass=Singleton):
    def __init__(self):
        ''' Initialize firebase '''
        # Set credentials
        ## serviceAccountKey (if rquired) to be generated from firebase -> Project Settings -> Service Accounts -> Generate new private key
        config = Config()["database"]["firebase"]
        cred = credentials.Certificate(config["service_account_key"])

        # Init app
        app = firebase_admin.initialize_app(cred, {
            "databaseURL": config["databaseURL"]
        })

    def getIssues(self):
        ''' Access database '''
        root = db.reference()
        issues = root.child("Yojaka/duke79/Issues")
        issues = issues.get()
        return issues

    def getUsers(self):
        ''' Login and access user '''
        users = auth.list_users()
        return users.users

    def getUserByUID(self, uid):
        return auth.get_user(uid)

    def get_user_uid_from_session(self, session_id):
        decoded_token = auth.verify_id_token(session_id)
        uid = decoded_token['uid']
        return uid
