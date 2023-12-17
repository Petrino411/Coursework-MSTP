import configparser

config = configparser.ConfigParser()
config.read("connect.ini")

BASE_URL = f"{str(config["Connection"]["BASE_URL"]).strip('"')}"




