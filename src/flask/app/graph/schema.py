# http://graphql.github.io/learn/queries/
# Avoid select * | Use IDs, let the child resolve its fields |
# https://weblogs.asp.net/jongalloway/the-real-reason-select-queries-are-bad-index-coverage

import graphene

from app.data import db
from app.data.permissions import UserPermission
from app.graph.category import Category, CategoriesAction
from app.graph.channel import Channel, ChannelsAction
from app.graph.user import User


class Query(graphene.ObjectType):
    channels = graphene.List(Channel, action=graphene.Argument(ChannelsAction, required=False, default_value={}))
    categories = graphene.List(Category, action=graphene.Argument(CategoriesAction, required=False, default_value={}))
    current_user = graphene.Field(User)

    def resolve_channels(self, info, action):
        channels = db.parse_all_channels()
        return channels  # TODO

    def resolve_categories(self, info, action):
        return [{"title": "asd"}]  # TODO

    def resolve_current_user(self, info):
        return {}  # TODO


schema = graphene.Schema(query=Query)
