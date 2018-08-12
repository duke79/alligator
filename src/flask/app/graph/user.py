import graphene
from app.data import db


class User(graphene.ObjectType):
    """User class for graph"""
    name = graphene.String()
    email = graphene.String()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def resolve_name(self, info):
        id = self["id"]
        user = db.get_user_by_id(id)
        return user["name"]

    def resolve_email(self, info):
        id = self["id"]
        user = db.get_user_by_id(id)
        return user["email"]
