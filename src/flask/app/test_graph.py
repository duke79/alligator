import json

import pytest


@pytest.fixture
def schema():
    from app.graph import schema
    return schema


class TestQuery():
#     def test_users(self, schema):
#         query = '''
#                 query SummonTheHeroes($prefix: String = "Bra") {
#                     heroes: users(prefix: $prefix){
#                         __typename
#                         ...userNameFra
#                     }
#                 }
#
#                 fragment userNameFra on User{
#                         name
#                         email
#                     }
#             '''
#
#         result = schema.execute(query)
#         result = json.dumps(result.data, indent=4)
#         assert result == """{
#     "heroes": [
#         {
#             "__typename": "User",
#             "name": "None",
#             "email": "None"
#         },
#         {
#             "__typename": "User",
#             "name": "None",
#             "email": "None"
#         },
#         {
#             "__typename": "User",
#             "name": "None",
#             "email": "None"
#         },
#         {
#             "__typename": "User",
#             "name": "None",
#             "email": "pulkitsinghbaliyan@hotmail.com"
#         },
#         {
#             "__typename": "User",
#             "name": "None",
#             "email": "None"
#         },
#         {
#             "__typename": "User",
#             "name": "None",
#             "email": "None"
#         },
#         {
#             "__typename": "User",
#             "name": "None",
#             "email": "None"
#         },
#         {
#             "__typename": "User",
#             "name": "None",
#             "email": "None"
#         },
#         {
#             "__typename": "User",
#             "name": "Pulkit Singh",
#             "email": "pulkitsingh01@gmail.com"
#         },
#         {
#             "__typename": "User",
#             "name": "None",
#             "email": "duke@gmail.com"
#         },
#         {
#             "__typename": "User",
#             "name": "None",
#             "email": "sdfdsf@dfsf.com"
#         },
#         {
#             "__typename": "User",
#             "name": "None",
#             "email": "None"
#         },
#         {
#             "__typename": "User",
#             "name": "None",
#             "email": "None"
#         },
#         {
#             "__typename": "User",
#             "name": "None",
#             "email": "None"
#         },
#         {
#             "__typename": "User",
#             "name": "None",
#             "email": "dukke79@gmail.com"
#         },
#         {
#             "__typename": "User",
#             "name": "None",
#             "email": "klsdjfldkj@dlfkjd.com"
#         },
#         {
#             "__typename": "User",
#             "name": "None",
#             "email": "None"
#         }
#     ]
# }"""

#     def test_users_schema(self, schema):
#         iQuery = '''
#                 {
#                     __schema {
#                         types {
#                             name
#                         }
#                     }
#                 }
#             '''
#         iresult = schema.execute(iQuery)
#         iresult = json.dumps(iresult.data, indent=4)
#
#         assert iresult == """{
#     "__schema": {
#         "types": [
#             {
#                 "name": "Query"
#             },
#             {
#                 "name": "User"
#             },
#             {
#                 "name": "String"
#             },
#             {
#                 "name": "__Schema"
#             },
#             {
#                 "name": "__Type"
#             },
#             {
#                 "name": "__TypeKind"
#             },
#             {
#                 "name": "Boolean"
#             },
#             {
#                 "name": "__Field"
#             },
#             {
#                 "name": "__InputValue"
#             },
#             {
#                 "name": "__EnumValue"
#             },
#             {
#                 "name": "__Directive"
#             },
#             {
#                 "name": "__DirectiveLocation"
#             }
#         ]
#     }
# }"""

    pass
