import os
from os import environ

API_ID = int(os.environ.get("API_ID", None))
API_HASH = os.environ.get("API_HASH", None)
DB_URI = os.environ.get("DATABASE_URL")
PHOTO = os.environ.get("PHOTO")
WORKERS = int(os.environ.get("WORKERS", 8))
ALLOW_EXCL = os.environ.get('ALLOW_EXCL', False)
ALLOW_CHATS = os.environ.get("ALLOW_CHATS", True)
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", None)
EVENT_LOGS = os.environ.get("EVENT_LOGS", None)
JOIN_LOGGER = os.environ.get("JOIN_LOGGER", None)
WEBHOOK = bool(os.environ.get("WEBHOOK", False))
CERT_PATH = os.environ.get("CERT_PATH")
URL = os.environ.get("URL", "")  # Does not contain token
PORT = int(os.environ.get("PORT", 5000))
LOAD = os.environ.get("LOAD", "").split()
NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
DEL_CMDS = bool(os.environ.get("DEL_CMDS", True))
INFOPIC = bool(os.environ.get("INFOPIC", True))
OWNER_ID = int(os.environ.get("OWNER_ID", None))
DEV_USERS = {int(x) for x in os.environ.get("DEV_USERS", "").split()}
SUDOERS = {int(x) for x in os.environ.get("SUDOERS", "").split()}
TOKEN = os.environ.get("TOKEN", None)
DONATION_LINK = os.environ.get("DONATION_LINK", None)

