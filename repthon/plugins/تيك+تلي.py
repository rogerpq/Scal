# Repthon🔥
# Repthon - Baqir
# Copyright (C) 2023 RepthonArabic . All Rights Reserved
#
# This file is a part of < https://github.com/RepthonArabic/RepthonAr/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/RepthonArabic/RepthonAr/blob/master/LICENSE/>.


import base64
import requests
import asyncio
import os
import sys
import urllib.request
from datetime import timedelta
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl.functions.messages import GetHistoryRequest, ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get


from repthon import zq_lo
from repthon.utils import admin_cmd
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import media_type
from ..helpers.utils import reply_id



#Code by T.me/E_7_V
@zq_lo.rep_cmd(pattern=f"تيك(?: |$)(.*)")
async def baqir_tiktok(event):
    TAIBA = event.pattern_match.group(1)
    if TAIBA: #Write Code By T.me/E_7_V
        ROGER = TAIBA
    elif event.is_reply:
        ROGER = await event.get_reply_message()
    else:
        return await edit_or_reply(event, "**⎉╎بالـࢪد ؏ــلى رابـط تيـك تـوك**")
    chat = "@downloader_tiktok_bot" #Code by T.me/E_7_V
    rep = await edit_or_reply(event, "**⎉╎جـارِ التحميـل من تيـك تـوك ...**")
    async with borg.conversation(chat) as conv: #Code by T.me/E_7_V
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(ROGER) #Code by T.me/E_7_V
            repthon = await conv.get_response()
            await rep.delete()
            await borg.send_file(
                event.chat_id,
                repthon,
                caption=f"<b>⎉╎تم تحميل الفيديـو .. بنجاح 🎬</b>",
                parse_mode="html",
            )
        except YouBlockedUserError: #Code by T.me/E_7_V
            await zq_lo(unblock("downloader_tiktok_bot"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(ROGER)
            repthon = await conv.get_response()
            await rep.delete()
            await borg.send_file(
                event.chat_id,
                repthon,
                caption=f"<b>⎉╎تم تحميل الفيديـو .. بنجاح 🎬</b>",
                parse_mode="html",
            )
# Write Code By telegram.dog/E_7_V ✌🏻
@zq_lo.on(admin_cmd(pattern="ستوري(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    j_link = event.pattern_match.group(1)
    if ".me" not in j_link:
        await event.edit("**⎉╎ يجب وضع رابط الستوري مع الامر اولا **")
    else:
        await event.edit("**⎉╎ يتم الان تنزيل الستوري انتظر قليلا**")
    chat = "@msaver_bot"
    async with zq_lo.conversation(chat) as conv:
        try:
            msg = await conv.send_message(j_link)
            video = await conv.get_response()
            """ تم تحميل الستوري بنجاح من قبل @Repthon """
            await zq_lo.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("**⎉╎ الغـي حـظر هـذا البـوت و حـاول مجـددا @msaver_bot**")
            return
        REPTHON = base64.b64decode("YnkzbDNyZXB0aG9uZG93bmxvYWQ=")
        TAIBA = Get(REPTHON)
        try:
            await event.client(TAIBA)
        except BaseException:
            pass
        await zq_lo.send_file(event.chat_id, video, caption=f"<b>⎉╎ BY : @Repthon 🎀</b>",parse_mode="html")
        await event.delete()
