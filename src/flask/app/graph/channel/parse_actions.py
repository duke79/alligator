from app.graph.channel.data import add_channel, remove_channel, update_channel, get_channels
from app.utils import safeDict


def parse_channels_actions(action):
    channels = []
    action_add = safeDict(action, ["add"])
    if action_add:
        add_channel(url=safeDict(action_add, ["url"]))

    action_remove = safeDict(action, ["remove"])
    if action_remove:
        remove_channel(id=safeDict(action_remove, ["id"]))

    action_update = safeDict(action, ["update"])
    if action_update:
        update_channel(id=safeDict(action_update, ["id"]),
                       url=safeDict(action_update, ["url"]),
                       categories=safeDict(action_update, ["categories"]))

    action_get = safeDict(action, ["get"])
    if action_get:
        channels = get_channels(ids=safeDict(action_get, ["ids"]),
                                category_id=safeDict(action_get, ["category_id"]),
                                match_in_url=safeDict(action_get, ["match_in_url"]),
                                limit=safeDict(action_get, ["limit"]))
    return channels
