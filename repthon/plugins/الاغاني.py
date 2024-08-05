# Repthon 🙈🔥

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
from . import zq_lo
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id


#الملـف كتابـة بـاقـر ⤶ @E_7_V خاص بسـورس ⤶ 𝙍𝙀𝙋𝙏𝙃𝙊𝙉
#الملف متعوب عليه So تخمط وماتذكـر المصـدر == اهينـك
@zq_lo.rep_cmd(pattern="اغنيه(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("**╮ جـارِ البحث ؏ـن الاغنيـٓه... 🎧♥️╰**")
    else:
        await event.edit("**╮ جـارِ البحث ؏ـن الاغنيـٓه... 🎧♥️╰**")
    chat = "@Repthon_YouTube_Robot"
    async with borg.conversation(chat) as conv: # code by t.me/E_7_V
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(d_link)
            await conv.get_response()
            await asyncio.sleep(5)
            baqir = await conv.get_response()
            if "⏳" not in baqir.text:
                await baqir.click(0)
                await asyncio.sleep(5)
                baqir = await conv.get_response()
                await event.delete()
                await borg.send_file(
                    event.chat_id,
                    baqir,
                    caption=f"**❈╎البحـث :** `{d_link}`",
                )

            else:
                await event.edit("**- لـم استطـع العثـور على نتائـج ؟!**\n**- حـاول مجـدداً في وقت لاحـق ...**")
        except YouBlockedUserError:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(d_link)
            await conv.get_response()
            await asyncio.sleep(5)
            baqir = await conv.get_response()
            baqir = await conv.get_response()
            if "⏳" not in baqir.text:
                await baqir.click(0)
                await asyncio.sleep(5)
                baqir = await conv.get_response()
                await event.delete()
                await borg.send_file(
                    event.chat_id,
                    baqir,
                    caption=f"**❈╎البحـث :** `{d_link}`",
                )

            else:
                await event.edit("**- لـم استطـع العثـور على نتائـج ؟!**\n**- حـاول مجـدداً في وقت لاحـق ...**")
