# http://graphql.github.io/learn/queries/
# Avoid select * | Use IDs, let the child resolve its fields |
# https://weblogs.asp.net/jongalloway/the-real-reason-select-queries-are-bad-index-coverage

import graphene

from app.data import db
from app.data.permissions import UserPermission
from app.graph.channel import Channel


class Query(graphene.ObjectType):
    channels = graphene.List(Channel)

    def resolve_channels(self, info):
        channels = db.parse_all_channels()
        return channels


schema = graphene.Schema(query=Query)
