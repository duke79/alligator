import graphene
from app.data import db
from app.graph.user import User


class Issue(graphene.ObjectType):
    project = graphene.String()
    count = graphene.Int()
    title = graphene.String()
    state = graphene.String()
    author = graphene.Field(User)
    created_at = graphene.String()
    updated_by = graphene.Field(User)
    updated_at = graphene.String()
    description = graphene.String()
    closed_at = graphene.String()
    closed_by = graphene.Field(User)
    discussion_locked = graphene.Boolean()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def resolve_project(self, info):
        issue_id = self["id"]
        issue = db.get_issue_by_id(issue_id)
        return issue["project"]

    def resolve_count(self, info):
        issue_id = self["id"]
        issue = db.get_issue_by_id(issue_id)
        return issue["count"]

    def resolve_title(self, info):
        issue_id = self["id"]
        issue = db.get_issue_by_id(issue_id)
        return issue["title"]

    def resolve_state(self, info):
        issue_id = self["id"]
        issue = db.get_issue_by_id(issue_id)
        return issue["state"]

    def resolve_author(self, info):
        issue_id = self["id"]
        issue = db.get_issue_by_id(issue_id)
        return {"id": issue["created_by_id"]}

    def resolve_created_at(self, info):
        issue_id = self["id"]
        issue = db.get_issue_by_id(issue_id)
        return issue["created_at"]

    def resolve_updated_by(self, info):
        issue_id = self["id"]
        issue = db.get_issue_by_id(issue_id)
        return {"id": issue["updated_by_id"]}

    def resolve_updated_at(self, info):
        issue_id = self["id"]
        issue = db.get_issue_by_id(issue_id)
        return issue["updated_at"]

    def resolve_description(self, info):
        issue_id = self["id"]
        issue = db.get_issue_by_id(issue_id)
        return issue["description"]

    def resolve_closed_at(self, info):
        issue_id = self["id"]
        issue = db.get_issue_by_id(issue_id)
        return issue["closed_at"]

    def resolve_closed_by(self, info):
        issue_id = self["id"]
        issue = db.get_issue_by_id(issue_id)
        return {"id": issue["closed_by_id"]}

    def resolve_discussion_locked(self, info):
        issue_id = self["id"]
        issue = db.get_issue_by_id(issue_id)
        if b'\x01' == issue["discussion_locked"]:
            return True
        else:
            return False


class IssueInput(graphene.InputObjectType):
    project_id = graphene.Int(required=True)
    count = graphene.Int(description="If not provided a new issue is created, otherwise existing issue is updated")
    title = graphene.String()
    state = graphene.String(description="open/closed")
    author_id = graphene.Int(required=True, description="Who is creating/updating the issue")
    description = graphene.String()
    discussion_locked = graphene.Boolean(description="true/false")


class CreateUpdateIssue(graphene.Mutation):
    """Create or update issue"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Arguments:
        issue_input = IssueInput(required=True)

    issue = graphene.Field(Issue)

    @staticmethod
    def mutate(root, info, issue_input=None):
        issue = None
        if not issue_input.count:
            issue = db.create_issue(project_id=issue_input.project_id,
                                    created_by_id=issue_input.author_id)
        else:
            issue = db.get_one_issue_by_project_and_count(project_id=issue_input.project_id,
                                                          count=issue_input.count)

        issue = db.update_issue(project_id=issue["project"],
                                count=issue["count"],
                                updated_by_id=issue_input.author_id,
                                title=issue_input.title,
                                state=issue_input.state,
                                description=issue_input.description,
                                discussion_locked=issue_input.discussion_locked)

        return CreateUpdateIssue(issue={"id": issue["id"]})
