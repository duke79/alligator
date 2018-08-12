# http://graphql.github.io/learn/queries/
# Avoid select * | Use IDs, let the child resolve its fields |
# https://weblogs.asp.net/jongalloway/the-real-reason-select-queries-are-bad-index-coverage

import graphene

from app.data import db
from app.data.permissions import UserPermission
from app.graph.issue import Issue, CreateUpdateIssue
from app.graph.user import User


class Query(graphene.ObjectType):
    users = graphene.List(User, prefix=graphene.String())
    issues = graphene.List(Issue, project_id=graphene.Int())

    def resolve_users(self, info, prefix):
        if db.check_permission(UserPermission.ALL.value):  # 1 = all
            return db.get_users_all(prefix=prefix)

    def resolve_issues(self, info, project_id):
        if db.check_permission(UserPermission.ALL.value):
            return db.get_issues_by_project_id(project_id=project_id)


class Mutations(graphene.ObjectType):
    create_update_issue = CreateUpdateIssue.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)

if __name__ == "__main__":
    query = '''
        query SummonTheHeroes($prefix: String = "Bra") {
            heroes: users(prefix: $prefix){
                __typename
                ...userNameFra
            }
        }
    
        fragment userNameFra on User{
                name
                email
            }     
    '''

    result = schema.execute(query)
    print(result.data)

    iQuery = '''
        {
            __schema {
                types {
                    name
                }
            }
        }
    '''
    result = schema.execute(iQuery)
    print(result.data)
