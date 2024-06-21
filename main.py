import datetime
import random
import threading
import time
import pyrogram
from config import api_id, api_key
import data
import sys


def get_message(app):
    for message in app.get_chat_history("me", limit=1):
        photo = None
        video = None
        try:
            photo = message.photo.file_id
        except:
            pass

        try:
            video = message.video.file_id
        except:
            pass

        text = message.text
        if (photo, video) != (None, None):
            text = message.caption

        if photo:
            return {"type": "photo", "text": text, "photo": photo}
        elif video:
            return {"type": "video", "text": text, "video": video}
        else:
            return {"type": "text", "text": text}


def last_message_is_not_our(app, group_id):
    for last_message in app.get_chat_history(group_id, limit=1):
        return last_message.from_user.id != app.get_me().id


def send_post(acc):
    with pyrogram.Client(name=str(acc), api_id=api_id, api_hash=api_key) as app:

        for i in [{"group": "@darkAdsRu",
                   "interval": random.randint(30*60, 60*60)}]:
            if last_message_is_not_our(app, i["group"]):
                message = get_message(app)
                if message:
                    try:
                        if message["type"] == "text":
                            app.send_message(i["group"], message["text"])
                        elif message["type"] == "photo":
                            app.send_photo(i["group"], message["photo"], caption=message["text"])
                        elif message["type"] == "video":
                            app.send_video(i["group"], message["video"], caption=message["text"])

                        print("\r[+]", "sended", f"({str(datetime.datetime.now())})")
                    except pyrogram.errors.exceptions.flood_420.SlowmodeWait:
                        pass
            time.sleep(i["interval"])


while True:
    send_post(sys.argv[1])
    time.sleep(10)