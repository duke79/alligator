import json
import os

from app.utils.singleton import Singleton


class ConfigError(Exception):
    pass


class Config(dict, metaclass=Singleton):
    def __str__(self):
        return json.dumps(self.config, indent=4)

    def __init__(self):
        dict.__init__(self, dict())  # Because dict is extended

        # Open <user>/.yojaka/config.json
        user_home = os.path.expanduser("~")
        self.config_dir = os.path.join(user_home, ".yojaka")
        self.config_file = os.path.join(self.config_dir, "config.json")

        if not os.path.exists(self.config_dir):
            os.mkdir(self.config_dir)

        # initialize self.config from config.json
        with open(self.config_file, "r+") as f:
            conf = f.read()
            if conf != "":
                try:
                    self.config = json.loads(conf)
                except json.decoder.JSONDecodeError as e:
                    raise ConfigError("Config file invalid format")
            else:
                self.config = dict()

    def __enter__(self):
        """ to enable 'with **' capability, counterpart function is __exit__ """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ commit at the end of 'with **' block """
        self.commit()

    def __getitem__(self, key):
        # return super().__getitem__(key)
        try:
            return self.config[key]
        except KeyError as e:
            self.__setitem__(key, dict())  # initialize the non-existent keys
            return self.config[key]

    def __setitem__(self, key, value):
        # super().__setitem__(key, value)
        self.config[key] = value

    def commit(self):
        """
        Commit the configuration changes to file
        Use "with Config() as config" if auto commit is needed at the end,
        otherwise use this method.
        """
        # make a copy of the original config
        from shutil import copyfile
        copyfile(self.config_file, self.config_file + ".old")

        # overwrite the file with new config
        with open(self.config_file, "w+") as f:
            json.dump(self.config, f, indent=4)


if __name__ == "__main__":
    with Config() as config:
        config["server"] = "http://dummy_server:port"
        config["database"] = {
            "mysql": {
                "user": "dummy_user",
                "host": "localhost",
                "password": "dummy_password"
            },
            "firebase": {
                "service_account_key": "path\\to\\service_account_key.json",
                "databaseURL": "https://dummy_db_url.firebaseio.com"
            }
        }
        config["debug"] = False

        # config.commit() #Not required, since we are using with*
