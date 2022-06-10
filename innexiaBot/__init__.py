import logging, os, sys, time
import telegram.ext as tg
from telethon.sessions import MemorySession
from telethon import TelegramClient


StartTime = time.time()


# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting."
    )
    quit(1)

    from config import *

    TOKEN = TOKEN
    try:
        OWNER_ID = int(OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")

    JOIN_LOGGER = JOIN_LOGGER
    ALLOW_CHATS = ALLOW_CHATS
    try:
        SUDOERS = set(int(x) for x in SUDOERS or [])
        DEV_USERS = set(int(x) for x in DEV_USERS or [])
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

 
# REQUIRED VARS TO START TELEGRAM BOT

    API_ID = API_ID
    API_HASH = API_HASH
    TOKEN = TOKEN
    DB_URI = SQLALCHEMY_DATABASE_URI

# REQUIRED VARS TO BRIDGE BOT AND SERVER

    WORKERS = Config.WORKERS
    ALLOW_EXCL = Config.ALLOW_EXCL
    WEBHOOK = Config.WEBHOOK
    CERT_PATH = Config.CERT_PATH
    PORT = Config.PORT
    URL = Config.URL

updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
telethn = TelegramClient(MemorySession(), API_ID, API_HASH)
dispatcher = updater.dispatcher
