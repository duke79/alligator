import graphene
from app.data import db
from app.utils import safeDict


class Category(graphene.ObjectType):
    id = graphene.Int()
    title = graphene.String()
    channels = graphene.List(
        'app.graph.channel.Channel')  # Circular solution: https://github.com/graphql-python/graphene/issues/522
    related_categories = graphene.List("app.graph.category.Category")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def resolve_id(self, info):
        return 0  # TODO

    def resolve_title(self, info):
        return "category_title"  # TODO

    def resolve_channels(self, info):
        # channels = db.parse_all_channels()
        # return channels
        return [""]  # TODO

    def resolve_related_categories(self, info):
        return [""]  # TODO
