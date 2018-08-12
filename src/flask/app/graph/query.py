# http://graphql.github.io/learn/queries/
# Avoid select * | Use IDs, let the child resolve its fields |
# https://weblogs.asp.net/jongalloway/the-real-reason-select-queries-are-bad-index-coverage

import graphene

from app.data import db
from app.data.permissions import UserPermission
from app.graph.news import News
from app.graph.user import User


class Query(graphene.ObjectType):
    feed = graphene.List(News)

    def resolve_feed(self, info):
        if db.check_permission(UserPermission.ALL.value):
            return [db.get_feed_by_id(i) for i in range(3)]


schema = graphene.Schema(query=Query)
