import graphene
from app.data import db
from app.graph.user.actions import UserCategoriesAction
from app.graph.user.parse_actions import parse_user_categories_actions


class UserSchema(graphene.ObjectType):
    """User class for graph"""
    name = graphene.String()
    email = graphene.String()
    categories = graphene.List("app.graph.category.schema.CategorySchema",
                               action=graphene.Argument(UserCategoriesAction, required=False, default_value={}))
    feed = graphene.List(graphene.String)

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

    def resolve_categories(self, info, action):
        return parse_user_categories_actions(action)  # TODO: User id must not come with action, but from session?

    def resolve_feed(self, info):
        return [""]  # TODO
