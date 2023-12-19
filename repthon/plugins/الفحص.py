# بس ابن الزنة وابن الحرام الي يغير حقوق
# ابن الكحبة الي يغير حقوقنا - @E_7_V - @rNrYr
# خصيمة يوم القيامة تبقى ذمة غير مسامح بها يوم الدين
import random
import re
import time
import os
from datetime import datetime
from platform import python_version
from random import choice

import requests
from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from repthon import StartTime, zq_lo, repversion

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import repalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus

plugin_category = "العروض"
ALIVE = gvarstatus("R_ALIVE") or "فحص"

# @E_7_V - # إضافة التاريخ كتابتي غير مبري الذمة الي ياخذه
file_path = "installation_date.txt"
if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    with open(file_path, "r") as file:
        installation_time = file.read().strip()
else:
    installation_time = datetime.now().strftime("%Y-%m-%d")
    with open(file_path, "w") as file:
        file.write(installation_time)

@zq_lo.rep_cmd(pattern=f"{ALIVE}$")
async def alive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    repevent = await edit_or_reply(event, "**𓅓┊جـاري .. فحـص البـوت الخـاص بك**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    R_EMOJI = gvarstatus("ALIVE_EMOJI") or "𓃰┊"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "بـوت ريبـــثون 𝐑𝐞𝐩𝐭𝐡𝐨𝐧 يعمـل .. بنجـاح ☑️ 𓆩"
    RANDOM_MEDIA = ["https://graph.org/file/f4c01d51562507a36c07e.mp4","https://graph.org/file/0b1e5679e24e735f870c5.mp4","https://graph.org/file/cafa0e8a1320891a65ae2.mp4","https://graph.org/file/b442b635cecca399dea39.mp4","https://graph.org/file/534d48ffb4b1e22e4ee39.mp4","https://graph.org/file/ec26c9d0a5532f17f85ac.mp4","https://graph.org/file/5201ed73785e5a928c853.mp4","https://graph.org/file/764e2427fafbe4aec2251.mp4","https://graph.org/file/9501d29c6cccd86b22686.mp4","https://graph.org/file/e30ff8013dd3f61f0735e.mp4","https://graph.org/file/3b9dc775779767faeb774.mp4","https://graph.org/file/1ee6a852367700b272a51.mp4","https://graph.org/file/53809263bafc29ef6adee.mp4","https://graph.org/file/4c6325935cb7e5494c77e.mp4","https://graph.org/file/a6a25238f38a351da1e33.mp4"] #@rNrYr
    ALIVE_TEXT=ALIVE_TEXT
    R_EMOJI=R_EMOJI
    uptime=uptime
    telever=version.__version__
    repver=repversion
    pyver=python_version()
    dbhealth=check_sgnirts
    ping=ms
    repthon_Tare5=installation_time # إضافة التاريخ كتابتي
    tgbot = Config.TG_BOT_USERNAME #@rNrYr اذكر حقوق يلا تخمط حقوق أحمد-دار
    me = await event.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    delete = await event.delete()
    user = await event.client.get_entity(event.chat_id)
    my_mention=my_mention
        

    
    final_message = f""" **{ALIVE_TEXT}**\n
**{R_EMOJI} قاعدۿ البيانات :** تعمل بنـجاح
**{R_EMOJI} إصـدار التـيليثون :** {telever}
**{R_EMOJI} إصـدار ريبـــثون :** {repver}
**{R_EMOJI} إصـدار البـايثون :** {pyver}
**{R_EMOJI} الوقـت :** {uptime}
**{R_EMOJI} المسـتخدم:** {my_mention}
**{R_EMOJI} التـاريـخ:** {repthon_Tare5}
**{R_EMOJI} الـبـوت: ** {tgbot}
**{R_EMOJI} قنـاة السـورس :** [اضغـط هنـا](https://t.me/Repthon)"""
    send_new_message = await event.client.send_message(entity=event.chat_id, message=final_message, file=random.choice(RANDOM_MEDIA)) #اذكر الحقوق @rNrYr حقوق أحمد-دار
