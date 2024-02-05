import re
from os import environ
import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client
from time import time

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]:
        return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Bot information
PORT = environ.get("PORT", "8080")
WEBHOOK = bool(environ.get("WEBHOOK", True))  # for web support on/off
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 60))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS' ,'https://graph.org/file/c3376ab143f7ded215412.jpg')).split()
BOT_START_TIME = time()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1782834874').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-100').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', "-1001715616229")
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Raj2345:Raj2345@cluster0.xyai6ld.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "animebash")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#maximum search result buttos count in number#
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "5"))
START_MESSAGE = environ.get('START_MESSAGE', '<b>Hello, {user}\n\nIm {bot}\nExplore, chat, and enjoy the anime world with us ✨</b>')
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", "Hey, {user},\n\n {query} This Is Not Your Searching Result\nSearch Yourself 👀")
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', '<b>Hey, {user}\n\nYou Have To Join My Updated Channel To Use Me</b>')
RemoveBG_API = environ.get("RemoveBG_API", "4atGShH49mDTN5R2fu6xfNZB")
WELCOM_PIC = environ.get("WELCOM_PIC", "https://graph.org/file/c3376ab143f7ded215412.jpg")
WELCOM_TEXT = environ.get("WELCOM_TEXT", "<b>Hey, {user}\n\nWelcome to {chat}\n\nDon't Spam Here Dear! Otherwise I will Ban You 😉</b>")
PMFILTER = environ.get('PMFILTER', "True")
G_FILTER = bool(environ.get("G_FILTER", True))
BUTTON_LOCK = environ.get("BUTTON_LOCK", "False")

# url shortner
SHORT_URL = environ.get("SHORT_URL", "")
SHORT_API = environ.get("SHORT_API", "")

# Others
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "180"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Anime_Bash_Chat')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
PM_IMDB = environ.get('PM_IMDB', "False")
IMDB = is_enabled((environ.get('IMDB', "False")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b>File Name : `{file_name}`\n\nSize - {file_size}\n\nAnime Provided By <a href=https://t.me/Anime_bash>[ Anime Bash ]</a></b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Query: {query}\n‌IMDb Data:\n\n🥂 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Release Year: <a href={url}/releaseinfo>{year}</a>\n🌟 IMDB Rating: <a href={url}/ratings>{rating}</a> / 10\n\nIMDB Data Provided By 👉 <a href= https://t.me/shinchanfilterrobot>ShinChan Filter Bot</a> 🥀</b>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

#request force sub
REQ_SUB = bool(environ.get("REQ_SUB", True))
SESSION_STRING = environ.get("SESSION_STRING", "BQDO2s4Asm80_5rpf8usDlkZd8Xc_vlBVcHemP5KlACJFTrYusMQMOWgRMgxTqyLVwGw9QFh1SvV0LTR4AKvN-PB1Tib8u_9ib_zo7nFETBUVDBCqVd2WMDkQifevPZMrZtnwoO8abuVurj5y_FbWJNdMuWQUEUlkOkdZsf3ConED2JcUIF25CUHjGk7ne1QeO8fbkVze3HjzOkVBJ0P-G_Jc0yPJEdn7aWrXMr1bt3IEP-sBK6wCp9BVUYlfjHgzOSghYxionE0p4SBsPC1uuyq853HrrHcc36JjYloDR1syxnIVos6U5vyZPDBjDz4Pv1fjywIcoIt3iPYO8lLY89-4AyvcAAAAAFzH0vbAQ")









