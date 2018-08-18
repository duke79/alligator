import graphene
from app.data import db
from app.utils import safeDict


class Filter(graphene.InputObjectType):
    all = graphene.Boolean(description="If True, all the existing categories are considered and "
                                       "not just the categories already opted by the user. Default : False",
                           default=False)
    query = graphene.String(description="To search categories by name.")


class ListActions(graphene.Enum):
    """
    ADD - To add categories
    REMOVE - To remove categories
    SET - To force set the categories to the provided list, replacing existing categories
    GET - To get categories, filtered by the provided filter (if provided)
    """
    ADD = 1
    REMOVE = 2
    SET = 3
    GET = 4


class Action(graphene.InputObjectType):
    type = ListActions(description="Type of action",
                       required=True)
    ids = graphene.List(graphene.Int, description="List of category ids against which the action "
                                                  "(ADD, REMOVE, SET) is to be performed.")
    filter = Filter(description="To help filter the GET result. If not filter is provided, "
                                "all categories opted by the user are returned.")


class Inputs(graphene.InputObjectType):
    action = graphene.Field(Action)


class Category(graphene.ObjectType):
    id = graphene.Int()
    channels = graphene.List(
        'app.graph.channel.Channel')  # Circular solution: https://github.com/graphql-python/graphene/issues/522
    related_categories = graphene.List("app.graph.category.Category")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def resolve_id(self, info):
        return 0

    def resolve_channels(self, info):
        # channels = db.parse_all_channels()
        # return channels
        return [""]

    def resolve_related_categories(self, info):
        return [""]
