import graphene

from app.graph.article.schema import ArticleSchema
from app.utils import safeDict


class ChannelSchema(graphene.ObjectType):
    """
    RSS Ref: https://validator.w3.org/feed/docs/rss2.html
    feedparser Ref: # https://pythonhosted.org/feedparser/reference.html
    """
    id = graphene.Int()
    title = graphene.String()
    link = graphene.String()
    description = graphene.String()
    language = graphene.String()
    copyright = graphene.String()
    managingEditor = graphene.String()
    webMaster = graphene.String()
    pubDate = graphene.String()
    publisher = graphene.String()
    lastBuildDate = graphene.String()
    category = graphene.List(graphene.String)  # TODO
    generator = graphene.String()
    docs = graphene.String()
    cloud = graphene.Field(graphene.String)  # TODO
    ttl = graphene.Field(graphene.String)  # TODO
    image = graphene.Field(graphene.String)  # TODO
    textInput = graphene.Field(graphene.String)  # TODO
    skipHours = graphene.String()
    skipDays = graphene.String()
    items = graphene.List(ArticleSchema)

    def resolve_id(self, info):
        return self.id

    def resolve_title(self, info):
        # return safeDict(self, ["feed", "title"])
        return self.title

    def resolve_link(self, info):
        # return safeDict(self, ["href"])
        return self.link

    def resolve_description(self, info):
        # return safeDict(self, ["feed", "subtitle"])
        return self.description

    def resolve_language(self, info):
        # return safeDict(self, ["feed", "language"])
        return self.language

    def resolve_copyright(self, info):
        # return safeDict(self, ["feed", "rights_detail"])
        return self.copyright

    def resolve_managingEditor(self, info):
        return ""

    def resolve_webMaster(self, info):
        return ""

    def resolve_pubDate(self, info):
        return safeDict(self, ["feed", "published"])  # TODO?

    def resolve_publisher(self, info):
        return safeDict(self, ["entries", "publisher"])  # TODO?

    def resolve_lastBuildDate(self, info):
        return ""

    def resolve_category(self, info):
        return safeDict(self, ["feed", "categories"])  # TODO?

    def resolve_generator(self, info):
        return safeDict(self, ["feed", "generator_detail", "name"])  # TODO?

    def resolve_docs(self, info):
        return safeDict(self, ["feed", "docs"])  # TODO?

    def resolve_cloud(self, info):
        return safeDict(self, ["feed", "cloud"])  # TODO?

    def resolve_ttl(self, info):
        return safeDict(self, ["feed", "ttl"])  # TODO?

    def resolve_image(self, info):
        return safeDict(self, ["feed", "image", "href"])  # TODO?

    def resolve_textInput(self, info):
        return safeDict(self, ["feed", "textinput"])  # TODO?

    def resolve_skipHour(self, info):
        return ""

    def resolve_skipDays(self, info):
        return ""

    def resolve_items(self, info):
        return safeDict(self, ["entries"])  # TODO?
