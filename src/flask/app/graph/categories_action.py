import graphene


class ActionAddCategory(graphene.InputObjectType):
    title = graphene.String()


class ActionRemoveCategory(graphene.InputObjectType):
    id = graphene.Int()


class ActionUpdateCategory(graphene.InputObjectType):
    id = graphene.Int(required=True)
    title = graphene.String()


class ActionGetCategories(graphene.InputObjectType):
    ids = graphene.List(graphene.Int, description="List of category ids to limit this action to.")
    query = graphene.String(description="To search categories by name.")
    channel_id = graphene.Int()
    limit = graphene.Int(default_value=10)


class CategoriesAction(graphene.InputObjectType):
    add = graphene.Field(ActionAddCategory)
    update = graphene.Field(ActionUpdateCategory)
    remove = graphene.Field(ActionRemoveCategory)
    get = graphene.Field(ActionGetCategories)
