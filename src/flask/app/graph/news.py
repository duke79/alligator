import graphene
from app.data import db

class News(graphene.ObjectType):
    title = graphene.String()
    picture = graphene.String()
    detail = graphene.String()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def resolve_title(self, info):
        # feed_id = self["id"]
        # feed = db.get_feed_by_id(feed_id)
        return self["title"]

    def resolve_picture(self, info):
        # feed_id = self["id"]
        # feed = db.get_feed_by_id(feed_id)
        return self["picture"]

    def resolve_detail(self, info):
        # feed_id = self["id"]
        # feed = db.get_feed_by_id(feed_id)
        return self["detail"]
