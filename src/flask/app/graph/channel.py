import graphene

from app.graph.newsitem import NewsItem
from app.data import db


def safeDict(elem, array_of_keys, default=""):
    try:
        for key in array_of_keys:
            elem = elem[key]
        return elem
    except Exception as e:
        return default


class Channel(graphene.ObjectType):
    """
    RSS Ref: https://validator.w3.org/feed/docs/rss2.html
    feedparser Ref: # https://pythonhosted.org/feedparser/reference.html
    """
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
    items = graphene.List(NewsItem)  # TODO

    def resolve_title(self, info):
        return safeDict(self, ["feed", "title"])

    def resolve_link(self, info):
        return safeDict(self, ["href"])

    def resolve_description(self, info):
        return safeDict(self, ["feed", "subtitle"])

    def resolve_language(self, info):
        return safeDict(self, ["feed", "language"])

    def resolve_copyright(self, info):
        return safeDict(self, ["feed", "rights_detail"])

    def resolve_managingEditor(self, info):
        return ""

    def resolve_webMaster(self, info):
        return ""

    def resolve_pubDate(self, info):
        return safeDict(self, ["feed", "published"])

    def resolve_publisher(self, info):
        return safeDict(self, ["entries", "publisher"])

    def resolve_lastBuildDate(self, info):
        return ""

    def resolve_category(self, info):
        return safeDict(self, ["feed", "categories"])

    def resolve_generator(self, info):
        return safeDict(self, ["feed", "generator_detail", "name"])

    def resolve_docs(self, info):
        return safeDict(self, ["feed", "docs"])

    def resolve_cloud(self, info):
        return safeDict(self, ["feed", "cloud"])

    def resolve_ttl(self, info):
        return safeDict(self, ["feed", "ttl"])

    def resolve_image(self, info):
        return safeDict(self, ["feed", "image", "href"])

    def resolve_textInput(self, info):
        return safeDict(self, ["feed", "textinput"])

    def resolve_skipHour(self, info):
        return ""

    def resolve_skipDays(self, info):
        return ""

    def resolve_items(self, info):
        return safeDict(self, ["entries"])
