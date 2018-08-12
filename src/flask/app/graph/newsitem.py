import graphene
from app.data import db

class NewsItem(graphene.ObjectType):
    channel = graphene.String()
    items = graphene.List(graphene.String)
    guid = graphene.String()
    date = graphene.String()
    date_parsed = graphene.String()
    description = graphene.String()
    description_detail = graphene.String()
    url = graphene.String()
    modified = graphene.String()
    modified_parsed = graphene.String()
    issued = graphene.String()
    issued_parsed = graphene.String()
    copyright = graphene.String()
    copyright_detail = graphene.String()
    tagline = graphene.String()
    tagline_detail = graphene.String()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def resolve_title(self, info):
        # feed_id = self["id"]
        # feed = db.get_feed_by_id(feed_id)
        return self["title"]

    def resolve_picture(self, info):
        # feed_id = self["id"]
        # feed = db.get_feed_by_id(feed_id)
        return self["media_content"][0]["url"]

    def resolve_detail(self, info):
        # feed_id = self["id"]
        # feed = db.get_feed_by_id(feed_id)
        return self["summary"]
