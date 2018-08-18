# http://graphql.github.io/learn/queries/
# Avoid select * | Use IDs, let the child resolve its fields |
# https://weblogs.asp.net/jongalloway/the-real-reason-select-queries-are-bad-index-coverage

import graphene

from app.data import db
from app.data.permissions import UserPermission
from app.graph.category import Category, Inputs
from app.graph.channel import Channel


class Query(graphene.ObjectType):
    channels = graphene.List(Channel)
    categories = graphene.List(Category, inputs=graphene.Argument(Inputs, required=False, default_value={}))

    def resolve_channels(self, info):
        channels = db.parse_all_channels()
        return channels

    def resolve_categories(self, info, inputs):
        pass
        return [{"title": "asd"}]


schema = graphene.Schema(query=Query)
