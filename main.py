from telethon.sync import TelegramClient
from telethon import functions, types
from TOKEN import *
import datetime


# global search
with TelegramClient(name, api_id, api_hash) as client:
    result = client(functions.messages.SearchGlobalRequest(
        q='Shavkat Mirziyoyev Qatar',
        filter=types.InputMessagesFilterEmpty(),
        min_date=datetime.datetime(2023, 6, 25),
        max_date=datetime.datetime(2023, 12, 18),
        offset_rate=0,
        offset_peer='username',
        offset_id=0,
        limit=5,
        folder_id=None
    ))
    print(result.stringify())



