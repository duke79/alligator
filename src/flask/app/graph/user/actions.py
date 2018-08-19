import graphene


class ActionAddUserCategories(graphene.InputObjectType):
    ids = graphene.List(graphene.Int)


class ActionRemoveUserCategories(graphene.InputObjectType):
    ids = graphene.List(graphene.Int)


class ActionUpdateUserCategories(graphene.InputObjectType):
    ids = graphene.List(graphene.Int)


class ActionGetUserCategories(graphene.InputObjectType):
    ids = graphene.List(graphene.Int, description="List of category ids to limit this action to.")
    query = graphene.String(description="To search categories by name.")
    channel_id = graphene.Int()
    limit = graphene.Int(default_value=10)


class UserCategoriesAction(graphene.InputObjectType):
    add = graphene.Field(ActionAddUserCategories)
    update = graphene.Field(ActionUpdateUserCategories)
    remove = graphene.Field(ActionRemoveUserCategories)
    get = graphene.Field(ActionGetUserCategories)