import graphene


class ActionAddUserCategories(graphene.InputObjectType):
    user_id = graphene.Int(required=True)
    category_ids = graphene.List(graphene.Int,
                                 required=True)


class ActionRemoveUserCategories(graphene.InputObjectType):
    user_id = graphene.Int(required=True)
    category_ids = graphene.List(graphene.Int,
                                 required=True)


class ActionUpdateUserCategories(graphene.InputObjectType):
    user_id = graphene.Int(required=True)
    category_ids = graphene.List(graphene.Int,
                                 required=True)


class ActionGetUserCategories(graphene.InputObjectType):
    user_id = graphene.Int(required=True)
    ids = graphene.List(graphene.Int, description="List of category ids to limit this action to.")
    query = graphene.String(description="To search categories by name.")
    channel_id = graphene.Int()
    limit = graphene.Int(default_value=10)


class UserCategoriesAction(graphene.InputObjectType):
    add = graphene.Field(ActionAddUserCategories)
    update = graphene.Field(ActionUpdateUserCategories)
    remove = graphene.Field(ActionRemoveUserCategories)
    get = graphene.Field(ActionGetUserCategories)
