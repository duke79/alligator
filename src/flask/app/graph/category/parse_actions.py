from app.graph.category.data import add_category, remove_category, update_category, get_categories
from app.utils import safeDict


def parse_categories_actions(action):
    categories = []
    action_add = safeDict(action, ["add"])
    if action_add:
        add_category(title=safeDict(action_add, ["title"]))

    action_remove = safeDict(action, ["remove"])
    if action_remove:
        remove_category(id=safeDict(action_remove, ["id"]))

    action_update = safeDict(action, ["update"])
    if action_update:
        update_category(id=safeDict(action_update, ["id"]),
                        title=safeDict(action_update, ["title"]))

    action_get = safeDict(action, ["get"])
    if action_get:
        categories = get_categories(ids=safeDict(action_get, ["ids"]),
                                    query=safeDict(action_get, ["query"]),
                                    channel_id=safeDict(action_get, ["channel_id"]),
                                    limit=safeDict(action_get, ["limit"]))
    return categories
