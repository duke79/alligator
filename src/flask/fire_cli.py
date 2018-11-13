import json
import sys

import fire
from app.data.db import DB

db = DB()


def json_dump(obj):
    print(json.dumps(obj, indent=4, sort_keys=True, default=str))  # https://stackoverflow.com/a/11875813/973425


class Users():
    def __init__(self):
        pass

    def name(self, id):
        ret = db.get_user_by_id(id)
        json_dump(ret)


class Root():
    """
    Root
    """
    cmd_history = []

    def __init__(self):
        self.channels = "u"
        self.users = Users()
        self.categories = "u"

    def dummy_json(self):
        obj = {
            "key1": [
                "val1",
                {
                    "key2": "val2",
                    "key3": 3.6
                }
            ]
        }
        json_dump(obj)

    def echo(self, arg):
        """
        JSON arg Tested : echo '{"a":"123", "tois":{"moins":12, "hil":["hodor", "mind"]}}'
        :param arg:
        :return:
        """
        json_dump(arg)

    def history(self):
        for cmd in Root.cmd_history:
            json_dump(cmd)


def main():
    if len(sys.argv) > 1:
        args = ""
        for arg in sys.argv[1:]:
            args += " " + arg
        fire.Fire(Root, args)
        Root.cmd_history.append(args)
    else:
        print("no args...")

    while True:
        cmd = input()
        fire.Fire(Root, cmd)
        Root.cmd_history.append(cmd)


if __name__ == "__main__":
    main()
