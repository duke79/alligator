# http://graphql.github.io/learn/queries/
# Avoid select * | Use IDs, let the child resolve its fields |
# https://weblogs.asp.net/jongalloway/the-real-reason-select-queries-are-bad-index-coverage

import graphene

from app.graph.channel.schema import ChannelSchema
from app.graph.channel.actions import ChannelsActions
from app.graph.channel.parse_actions import parse_channels_actions
from app.graph.category.schema import CategorySchema
from app.graph.category.actions import CategoriesActions
from app.graph.category.parse_actions import parse_categories_actions
from app.graph.user.schema import UserSchema


class Query(graphene.ObjectType):
    channels = graphene.List(ChannelSchema,
                             action=graphene.Argument(ChannelsActions,
                                                      required=False,
                                                      default_value={}))
    categories = graphene.List(CategorySchema,
                               action=graphene.Argument(CategoriesActions,
                                                        required=False,
                                                        default_value={}))
    current_user = graphene.Field(UserSchema)

    def resolve_channels(self, info, action):
        return parse_channels_actions(action)

    def resolve_categories(self, info, action):
        return parse_categories_actions(action)

    def resolve_current_user(self, info):
        return {}  # TODO


schema = graphene.Schema(query=Query)
