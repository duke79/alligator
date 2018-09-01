import os


class Paths():
    @staticmethod
    def flask_root():
        file_dir = os.path.abspath(__file__)
        flask_dir = os.path.dirname(os.path.dirname(os.path.dirname(file_dir)))
        return flask_dir
