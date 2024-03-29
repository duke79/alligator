import graphene
from app.data import db
from app.data.tables.category import Category
from app.data.tables.channel import Channel
from app.data.tables.channel_categories import ChannelCategories
from app.graph.category.schema import CategorySchema
from app.utils import safeDict


class ArticleSchema(graphene.ObjectType):
    id = graphene.Int()
    title = graphene.String()
    link = graphene.String()
    description = graphene.String()
    author = graphene.String()
    category = graphene.String()
    comments = graphene.List(graphene.String)
    enclusures = graphene.String()
    guid = graphene.String()
    pubDate = graphene.String()
    source = graphene.String()
    media_content = graphene.List(graphene.String)  # TODO

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def resolve_id(self, info):
        return safeDict(self, ["id"])

    def resolve_title(self, info):
        return safeDict(self, ["article"])

    def resolve_link(self, info):
        return safeDict(self, ["link"])

    def resolve_description(self, info):
        return safeDict(self, ["summary"])

    def resolve_author(self, info):
        return safeDict(self, ["author_detail"])

    def resolve_category(self, info):
        category = safeDict(self, ["category"])
        # categories = Channel.session().query(Category).join(ChannelCategories).join(Channel).filter(Channel.id == channel_id).all()
        return category

    def resolve_comments(self, info):
        return safeDict(self, ["comments"])

    def resolve_enclusures(self, info):
        return safeDict(self, ["comments"])

    def resolve_guid(self, info):
        return safeDict(self, ["id"])

    def resolve_pubDate(self, info):
        return safeDict(self, ["published"])

    def resolve_source(self, info):
        return safeDict(self, ["source"])

    def resolve_media_content(self, info):
        return safeDict(self, ["media_content"])
