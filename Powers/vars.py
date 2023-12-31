from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default="6356729797:AAGdtemVDDyL5C1o6ZXhFkrjwj7FNPy-uH8")
    API_ID = int(config("API_ID", default="29098103"))
    API_HASH = config("API_HASH", default="06baef4020832888ccf3ebf4e746d52b")
    OWNER_ID = int(config("OWNER_ID", default=5332414680))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP", default=-1001932566732))
    DEV_USERS = [
        int(i)
        for i in config(
            "DEV_USERS",
            default="5332414680",
        ).split(" ")
    ]
    SUDO_USERS = [
        int(i)
        for i in config(
            "SUDO_USERS",
            default="5191699870",
        ).split(" ")
    ]
    WHITELIST_USERS = [
        int(i)
        for i in config(
            "WHITELIST_USERS",
            default="1103636187",
        ).split(" ")
    ]
    GENIUS_API_TOKEN = config("GENIUS_API",default="_SKHd_-xt05rO7pSt2Zvx4pL1_MoBOYWjOOPd-pQ1zinaHzmOYBajdVa_rrBKJgl")
    AuDD_API = config("AuDD_API",default="02342fd5abeb2840f7ff0522a6d8c55f")
    RMBG_API = config("RMBG_API",default="qjzqR82wn2BCkxUazpQ7vP5H")
    DB_URI = config("DB_URI", default="mongodb+srv://godgamer9434:tyWW0y2JPB0w7uDu@cluster0.hhmcouj.mongodb.net/?retryWrites=true&w=majority")
    DB_NAME = config("DB_NAME", default="godgamer9434")
    BDB_URI = config("BDB_URI",default="mongodb+srv://Armaan:tTdI4C2FTHACLmVB@cluster0.ymwrzo1.mongodb.net/?retryWrites=true&w=majority")
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="Grab_Your_WH_Group")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="WofBotsUpdates")
    WORKERS = int(config("WORKERS", default=16))
    TIME_ZONE = config("TIME_ZONE",default='Asia/Kolkata')
    BOT_USERNAME = "Gojo_Satoru_The_Honoured_One_Bot"
    BOT_ID = "6356729797"
    BOT_NAME = "Gojo Satoru"
    owner_username = "Armaan512"


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "6356729797:AAGdtemVDDyL5C1o6ZXhFkrjwj7FNPy-uH8"
    API_ID = 29098103  # Your APP_ID from Telegram
    API_HASH = "06baef4020832888ccf3ebf4e746d52b"  # Your APP_HASH from Telegram
    OWNER_ID = 5332414680  # Your telegram user id defult to mine
    MESSAGE_DUMP = -1001932566732  # Your Private Group ID for logs
    DEV_USERS = [5332414680]
    SUDO_USERS = [5191699870]
    WHITELIST_USERS = [1103636187]
    DB_URI = "mongodb+srv://godgamer9434:tyWW0y2JPB0w7uDu@cluster0.hhmcouj.mongodb.net/?retryWrites=true&w=majority"  # Your mongo DB URI
    DB_NAME = "godgamer9434"  # Your DB name
    NO_LOAD = []
    GENIUS_API_TOKEN = "_SKHd_-xt05rO7pSt2Zvx4pL1_MoBOYWjOOPd-pQ1zinaHzmOYBajdVa_rrBKJgl"
    RMBG_API = "qjzqR82wn2BCkxUazpQ7vP5H"
    AuDD_API = "02342fd5abeb2840f7ff0522a6d8c55f"
    PREFIX_HANDLER = ["!", "/","$"]
    SUPPORT_GROUP = "Grab_Your_WH_Group"
    SUPPORT_CHANNEL = "WofBotsUpdates"
    VERSION = "VERSION"
    TIME_ZONE = 'Asia/Kolkata'
    BDB_URI = "mongodb+srv://Armaan:tTdI4C2FTHACLmVB@cluster0.ymwrzo1.mongodb.net/?retryWrites=true&w=majority"
    WORKERS = 8
