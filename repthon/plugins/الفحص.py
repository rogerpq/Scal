# بس ابن الزنة وابن الحرام الي يغير حقوق
# ابن الكحبة الي يغير حقوقنا - @E_7_V - @rNrYr
# خصيمة يوم القيامة تبقى ذمة غير مسامح بها يوم الدين
import random
import re
import time
import psutil
from datetime import datetime
from platform import python_version

import requests
from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from . import StartTime, zq_lo, repversion

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import repalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_category = "العروض"
STATS = gvarstatus("R_STATS") or "فحص"


@zq_lo.rep_cmd(pattern=f"{STATS}$")
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    start = datetime.now()
    repevent = await edit_or_reply(event, "**𓅓┊جـارِ .. فحـص البـوت الخـاص بك**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    if gvarstatus("r_date") is not None:
        rrd = gvarstatus("r_date")
        rrt = gvarstatus("r_time")
        repda = f"{rrd}┊{rrt}"
    else:
        repda = f"{bt.year}/{bt.month}/{bt.day}"
    R_EMOJI = gvarstatus("ALIVE_EMOJI") or "𓃰┊"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "**بـوت ريبـــثون 𝗥𝗘𝗣𝗧𝗛𝗢𝗡  يعمـل .. بنجـاح ☑️ 𓆩 **"
    REP_IMG = gvarstatus("ALIVE_PIC")
    rep_caption = gvarstatus("ALIVE_TEMPLATE") or rep_temp
    caption = rep_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        R_EMOJI=R_EMOJI,
        mention=mention,
        uptime=uptime,
        repda=repda,
        telever=version.__version__,
        repver=repversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if REP_IMG:
        REP = [x for x in REP_IMG.split()]
        PIC = random.choice(REP)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await repevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                zedevent,
                f"**⌔∮ عـذراً عليـك الـرد ع صـوره او ميـديـا  ⪼  `.اضف صورة الفحص` <بالرد ع الصـوره او الميـديـا> ",
            )
    else:
        await edit_or_reply(
            repevent,
            caption,
        )


rep_temp = """{ALIVE_TEXT}

**{R_EMOJI} قاعدة البيانات :** تعمـل بـ نجـاح ♾
**{R_EMOJI} إصـدار المكتبـه :** `{telever}`
**{R_EMOJI} إصـدار السـورس :** `{repver}`
**{R_EMOJI} إصـدار بايثـون :** `{pyver}`
**{R_EMOJI} وقت التشغيل :** `{uptime}`
**{R_EMOJI} تاريـخ التنصيب :** `{repda}`
**{R_EMOJI} المسـتخـدم:** {mention}
**{R_EMOJI} قنـاة السـورس :** [اضغـط هنـا](https://t.me/Repthon)"""


@zq_lo.rep_cmd(
    pattern="الفحص$",
    command=("الفحص", plugin_category),
    info={
        "header": "- لـ التحـقق من ان البـوت يعمـل بنجـاح .. بخـاصيـة الانـلايـن ✓",
        "الاسـتخـدام": [
            "{tr}الفحص",
        ],
    },
)
async def amireallyialive(event):
    "A kind of showing bot details by your inline bot"
    reply_to_id = await reply_id(event)
    R_EMOJI = gvarstatus("ALIVE_EMOJI") or "𓅓┊"
    rep_caption = "** بـوت ريبـــثون 𝗥𝗘𝗣𝗧𝗛𝗢𝗡  يعمـل .. بنجـاح ☑️ 𓆩 **\n"
    rep_caption += f"**{R_EMOJI} إصـدار التـيليثون :** `{version.__version__}\n`"
    rep_caption += f"**{R_EMOJI} إصـدار ريبـــثون :** `{repversion}`\n"
    rep_caption += f"**{R_EMOJI} إصـدار البـايثون :** `{python_version()}\n`"
    rep_caption += f"**{R_EMOJI} المسـتخدم :** {mention}\n"
    results = await event.client.inline_query(Config.TG_BOT_USERNAME, rep_caption)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


@zq_lo.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await repalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
