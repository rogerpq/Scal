import json
import os
import re

from telethon.events import CallbackQuery

from repthon import zq_lo


@zq_lo.tgbot.on(CallbackQuery(data=re.compile(b"secret_(.*)")))
async def on_plug_in_callback_query_handler(event):
    timestamp = int(event.pattern_match.group(1).decode("UTF-8"))
    if os.path.exists("./repthon/secrets.txt"):
        jsondata = json.load(open("./repthon/secrets.txt"))
        try:
            message = jsondata[f"{timestamp}"]
            userid = message["userid"]
            ids = [userid, zq_lo.uid]
            if event.query.user_id in ids:
                encrypted_tcxt = message["text"]
                reply_pop_up_alert = encrypted_tcxt
            else:
                reply_pop_up_alert = "دعبـل مطـي الهمسـه مـو الك 🧑🏻‍🦯🦓"
        except KeyError:
            reply_pop_up_alert = "اووبس .. هذه الرسـالة لم تعد موجـوده"
    else:
        reply_pop_up_alert = "اووبس .. هـذه الرسـالة لم تعد موجـودة "
    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
