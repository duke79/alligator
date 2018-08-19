from app.graph.user.data import get_user_categories, update_user_categories, remove_user_categories, add_user_categories
from app.utils import safeDict


def parse_user_categories_actions(action):
    categories = []
    action_add = safeDict(action, ["add"])
    if action_add:
        add_user_categories(user_id=safeDict(action_add, ["user_id"]),
                            category_ids=safeDict(action_add, ["category_ids"]))

    action_remove = safeDict(action, ["remove"])
    if action_remove:
        remove_user_categories(user_id=safeDict(action_remove, ["user_id"]),
                               category_ids=safeDict(action_remove, ["category_ids"]))

    action_update = safeDict(action, ["update"])
    if action_update:
        update_user_categories(user_id=safeDict(action_update, ["user_id"]),
                               category_ids=safeDict(action_update, ["category_ids"]))

    action_get = safeDict(action, ["get"])
    if action_get:
        categories = get_user_categories(user_id=safeDict(action_get, ["user_id"]),
                                         category_ids=safeDict(action_get, ["category_ids"]),
                                         query=safeDict(action_get, ["query"]),
                                         channel_id=safeDict(action_get, ["channel_id"]),
                                         limit=safeDict(action_get, ["limit"]))
    return categories
