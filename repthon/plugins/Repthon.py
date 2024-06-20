import json
import math
import os
import random
import re
import time
from pathlib import Path
from uuid import uuid4

from telethon import Button, types
from telethon.errors import QueryIdInvalidError
from telethon.events import CallbackQuery, InlineQuery

from . import zq_lo
from ..Config import Config
from ..helpers.functions import rand_key
from ..sql_helper.globals import gvarstatus
from ..core.logger import logging

LOGS = logging.getLogger(__name__)
BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")
MEDIA_PATH_REGEX = re.compile(r"(:?\<\bmedia:(:?(?:.*?)+)\>)")
tr = Config.COMMAND_HAND_LER

def ibuild_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb

@zq_lo.tgbot.on(InlineQuery)
async def inline_handler(event):  # sourcery no-metrics
    builder = event.builder
    result = None
    query = event.text
    string = query.lower()
    query.split(" ", 2)
    str_y = query.split(" ", 1)
    string.split()
    query_user_id = event.query.user_id
    if query_user_id == Config.OWNER_ID or query_user_id in Config.SUDO_USERS:
        if string == "pmpermit":
            controlpmch = gvarstatus("pmchannel") or None
            if controlpmch is not None:
                rchannel = controlpmch.replace("@", "")
                buttons = [[Button.url("⌔ قنـاتـي ⌔", f"https://t.me/{rchannel}")]]
            else:
                buttons = [[Button.url("𝗦𝗼𝘂𝗿𝗰𝗲 𝗥𝗲𝗽𝘁𝗵𝗼𝗻", "https://t.me/Repthon")]]
            PM_PIC = gvarstatus("pmpermit_pic")
            if PM_PIC:
                CAT = [x for x in PM_PIC.split()]
                PIC = list(CAT)
                RRR_IMG = random.choice(PIC)
            else:
                RRR_IMG = None
            query = gvarstatus("pmpermit_text")
            if RRR_IMG and RRR_IMG.endswith((".jpg", ".jpeg", ".png")):
                result = builder.photo(
                    RRR_IMG,
                    # title="Alive rrr",
                    text=query,
                    buttons=buttons,
                )
            elif ZZZ_IMG:
                result = builder.document(
                    ZZZ_IMG,
                    title="Alive rrr",
                    text=query,
                    buttons=buttons,
                )
            else:
                result = builder.article(
                    title="Alive rrr",
                    text=query,
                    buttons=buttons,
                )
            await event.answer([result] if result else None)
