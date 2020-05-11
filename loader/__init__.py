import yaml


class Authentication(object):
    def __init__(self, config: dict):
        # Postgres
        self.HOST = config["QBITTORRENT"]["HOST"]
        self.USER = config["QBITTORRENT"]["USER"]
        self.PASSWORD = config["QBITTORRENT"]["PASS"]


def load_config(filename):
    with open(filename) as f:
        config = yaml.safe_load(f)
    return Authentication(config)
