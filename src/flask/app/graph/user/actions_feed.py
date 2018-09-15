import graphene


class SortField(graphene.Enum):
    PUBLISHED_DATE = 0
    UPDATED_DATE = 1
    TITLE = 2
    CATEGORY = 3
    CHANNEL_URL = 4


class ActionGetFeed(graphene.InputObjectType):
    user_id = graphene.Int(required=True)
    sort_by = graphene.List(SortField,
                            description="List of fields to be sorted by. Subsequent entries in this list have lower priority.")
    sort_order = graphene.List(graphene.Boolean,
                               description="order list mapped with sort_by. True for ascending order, False for descending")
    limit = graphene.Int(default_value=10)
    offset = graphene.Int(default_value=0)


class UserFeedAction(graphene.InputObjectType):
    get = graphene.Field(ActionGetFeed)
