
import os

class Config:

    BOT_TOKEN = os.environ.get('BOT_TOKEN', "")
    APP_ID = os.environ.get('APP_ID', "3335796")
    API_HASH = os.environ.get('API_HASH', "138b992a0e672e8346d8439c3f42ea78")

    #comma seperated user id of users who are allowed to use

    DOWNLOAD_DIR = 'downloads'
    OWNER_ID = int(os.environ.get("OWNER_ID", 1316963576))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001792962793")  
    # your telegram id
    OWNER_ID = int(os.environ.get("OWNER_ID", ""))
    # database session name, example: xurluploader
    SESSION_NAME = os.environ.get("SESSION_NAME", "")
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://abirhasan2005:abirhasan@cluster0.i6qzp.mongodb.net/cluster0?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001792962793"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
    DOWNLOAD_LOCATION = "./DOWNLOADS"
