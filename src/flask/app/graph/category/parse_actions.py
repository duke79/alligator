from app.graph.category.data import add_category, remove_category, update_category, get_categories
from app.utils import safeDict


def parse_categories_actions(action):
    channels = []
    action_add = safeDict(action, ["add"])
    if action_add:
        add_category(url=safeDict(action_add, ["url"]))

    action_remove = safeDict(action, ["remove"])
    if action_remove:
        remove_category(id=safeDict(action_remove, ["id"]))

    action_update = safeDict(action, ["update"])
    if action_update:
        update_category(id=safeDict(action_update, ["id"]),
                        url=safeDict(action_update, ["url"]),
                        categories=safeDict(action_update, ["categories"]))

    action_get = safeDict(action, ["get"])
    if action_get:
        channels = get_categories(ids=safeDict(action_update, ["ids"]),
                                  category_id=safeDict(action_update, ["category_id"]),
                                  match_in_url=safeDict(action_update, ["match_in_url"]),
                                  limit=safeDict(action_update, ["limit"]))
    return channels
