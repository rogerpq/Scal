# بس ابن الزنة وابن الحرام الي يغير حقوق
# ابن الكحبة الي يغير حقوقنا - @E_7_V
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

from . import StartTime, zq_lo, repversion

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import repalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus

plugin_category = "العروض"
STATS = gvarstatus("R_STATS") or "فحص"


@zq_lo.rep_cmd(pattern=f"{STATS}$")
async def rep_alive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    start = datetime.now()
    repevent = await edit_or_reply(event, "**⎆┊جـاري .. فحـص البـوت الخـاص بك**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    if gvarstatus("r_date") is not None:
        rrd = gvarstatus("r_date")
        rrt = gvarstatus("r_time")
        reppa = f"{rrd}┊{rrt}"
    else:
        reppa = f"{bt.year}/{bt.month}/{bt.day}"
    R_EMOJI = gvarstatus("ALIVE_EMOJI") or "✥┊"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "** بـوت ريبـــثون 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 يعمـل .. بنجـاح ☑️ 𓆩 **"
    REP_IMG = gvarstatus("ALIVE_PIC")
    USERID = zq_lo.uid if Config.OWNER_ID == 0 else Config.OWNER_ID
    ALIVE_NAME = gvarstatus("ALIVE_NAME") if gvarstatus("ALIVE_NAME") else "-"
    mention = f"[{ALIVE_NAME}](tg://user?id={USERID})"
    rep_caption = gvarstatus("ALIVE_TEMPLATE") or rep_temp
    caption = rep_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        R_EMOJI=R_EMOJI,
        mention=mention,
        uptime=uptime,
        reppa=rrd,
        rrd=rrd,
        rrt=rrt,
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
                repevent,
                f"**⌔∮ عـذراً عليـك الـرد ع صـوره او ميـديـا  ⪼  `.اضف صورة الفحص` <بالرد ع الصـوره او الميـديـا> ",
            )
    else:
        await edit_or_reply(
            repevent,
            caption,
        )


rep_temp = """
┏───────────────┓
│ ◉ ʙᴏᴛ ʀᴇᴘᴛʜᴏɴ ɪs ʀᴜɴɴɪɴɢ ɴᴏᴡ
┣───────────────┫
│ ● ɴᴀᴍᴇ ➪  {mention}
│ ● ʀᴇᴘᴛʜᴏɴ ➪ {repver}
│ ● ᴘʏᴛʜᴏɴ ➪ {pyver}
│ ● ᴘʟᴀᴛғᴏʀᴍ ➪ 𐌺᧐yᥱδ
│ ● ᴘɪɴɢ ➪ {ping}
│ ● ᴜᴘ ᴛɪᴍᴇ ➪ {uptime}
│ ● ᴀʟɪᴠᴇ sɪɴᴇᴄ ➪ {reppa}
│ ● ᴍʏ ᴄʜᴀɴɴᴇʟ ➪ [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/Repthon)
┗───────────────┛"""
