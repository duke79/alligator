import graphene


class ActionAddChannel(graphene.InputObjectType):
    url = graphene.String(description="RSS feed ulr",
                          required=True)
    categories = graphene.List(graphene.Int,
                               description="List of categories that this channel is part of")


class ActionRemoveChannel(graphene.InputObjectType):
    id = graphene.Int(required=True)


class ActionUpdateChannel(graphene.InputObjectType):
    id = graphene.Int(required=True)
    url = graphene.String(description="RSS feed ulr")
    categories = graphene.List(graphene.Int,
                               description="List of categories that this channel is part of")


class ActionGetChannels(graphene.InputObjectType):
    ids = graphene.List(graphene.Int, description="List of channel ids to limit this action to.")
    category_id = graphene.Int()
    match_in_url = graphene.String(description="To search through URLs by the provided string")
    limit = graphene.Int(default_value=10)


class ChannelsActions(graphene.InputObjectType):
    add = graphene.Field(ActionAddChannel)
    remove = graphene.Field(ActionRemoveChannel)
    update = graphene.Field(ActionUpdateChannel)
    get = graphene.Field(ActionGetChannels)

