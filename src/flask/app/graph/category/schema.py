import graphene
from app.data import db
from app.utils import safeDict


class CategorySchema(graphene.ObjectType):
    id = graphene.Int()
    title = graphene.String()
    channels = graphene.List(
        'app.graph.channel.schema.ChannelSchema')  # Circular solution: https://github.com/graphql-python/graphene/issues/522
    related_categories = graphene.List("app.graph.category.schema.CategorySchema")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def resolve_id(self, info):
        return safeDict(self, ["id"])

    def resolve_title(self, info):
        return safeDict(self, ["title"])

    def resolve_channels(self, info):
        # channels = db.parse_all_channels()
        # return channels
        return [""]  # TODO

    def resolve_related_categories(self, info):
        return [""]  # TODO
