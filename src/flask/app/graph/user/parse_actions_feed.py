from app.graph.user.data_feed import get_user_feed
from app.utils import safeDict


def parse_user_feed_actions(action):
    feed = []
    action_get = safeDict(action, ["get"])
    if action_get:
        feed = get_user_feed(user_id=safeDict(action_get, ["user_id"]),
                             sort_by=safeDict(action_get, ["sort_by"]),
                             sort_order=safeDict(action_get, ["sort_order"]),
                             limit=safeDict(action_get, ["limit"]),
                             offset=safeDict(action_get, ["offset"]))
    return feed
