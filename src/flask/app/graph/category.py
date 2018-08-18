import graphene
from app.data import db
from app.utils import safeDict


class ActionAddCategory(graphene.InputObjectType):
    title = graphene.String()


class ActionRemoveCategory(graphene.InputObjectType):
    id = graphene.Int()


class ActionUpdateCategory(graphene.InputObjectType):
    id = graphene.Int(required=True)
    title = graphene.String()


class ActionGetCategories(graphene.InputObjectType):
    ids = graphene.List(graphene.Int, description="List of category ids to limit this action to.")
    query = graphene.String(description="To search categories by name.")
    channel_id = graphene.Int()
    limit = graphene.Int(default_value=10)


class CategoriesAction(graphene.InputObjectType):
    add = graphene.Field(ActionAddCategory)
    update = graphene.Field(ActionUpdateCategory)
    remove = graphene.Field(ActionRemoveCategory)
    get = graphene.Field(ActionGetCategories)


class Category(graphene.ObjectType):
    id = graphene.Int()
    title = graphene.String()
    channels = graphene.List(
        'app.graph.channel.Channel')  # Circular solution: https://github.com/graphql-python/graphene/issues/522
    related_categories = graphene.List("app.graph.category.Category")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def resolve_id(self, info):
        return 0

    def resolve_title(self, info):
        return "category_title"

    def resolve_channels(self, info):
        # channels = db.parse_all_channels()
        # return channels
        return [""]

    def resolve_related_categories(self, info):
        return [""]
