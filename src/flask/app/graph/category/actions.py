import graphene


class CategoriesActionAdd(graphene.InputObjectType):
    title = graphene.String()


class CategoriesActionRemove(graphene.InputObjectType):
    id = graphene.Int()


class CategoriesActionUpdate(graphene.InputObjectType):
    id = graphene.Int(required=True)
    title = graphene.String()


class CategoriesActionGet(graphene.InputObjectType):
    ids = graphene.List(graphene.Int, description="List of category ids to limit this action to.")
    query = graphene.String(description="To search categories by name.")
    channel_id = graphene.Int()
    limit = graphene.Int(default_value=10)


class CategoriesActions(graphene.InputObjectType):
    add = graphene.Field(CategoriesActionAdd)
    update = graphene.Field(CategoriesActionUpdate)
    remove = graphene.Field(CategoriesActionRemove)
    get = graphene.Field(CategoriesActionGet)

