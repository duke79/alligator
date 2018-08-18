import graphene
from app.data import db


class ActionAddUserCategories(graphene.InputObjectType):
    id = graphene.List(graphene.Int)


class ActionRemoveUserCategories(graphene.InputObjectType):
    id = graphene.List(graphene.Int)


class ActionUpdateUserCategories(graphene.InputObjectType):
    id = graphene.List(graphene.Int)


class ActionGetUserCategories(graphene.InputObjectType):
    ids = graphene.List(graphene.Int, description="List of category ids to limit this action to.")
    query = graphene.String(description="To search categories by name.")
    channel_id = graphene.Int()
    limit = graphene.Int(default_value=10)


class UserCategoriesAction(graphene.InputObjectType):
    add = graphene.Field(ActionAddUserCategories)
    update = graphene.Field(ActionUpdateUserCategories)
    remove = graphene.Field(ActionRemoveUserCategories)
    get = graphene.Field(ActionGetUserCategories)


class User(graphene.ObjectType):
    """User class for graph"""
    name = graphene.String()
    email = graphene.String()
    categories = graphene.List("app.graph.category.Category", action=graphene.Argument(UserCategoriesAction, required=False, default_value={}))

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
