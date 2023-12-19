import asyncio
import contextlib
from datetime import datetime

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
from telethon.utils import get_display_name

from . import zq_lo

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _format
from ..sql_helper import gban_sql_helper as gban_sql
from ..sql_helper.mute_sql import is_muted, mute, unmute
from . import BOTLOG, BOTLOG_CHATID, admin_groups, get_user_from_event

plugin_category = "الادمن"

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

rep_dev = (5502537272, 5502537272)


@zq_lo.rep_cmd(
    pattern="ح عام(?:\s|$)([\s\S]*)",
    command=("gban", plugin_category),
    info={
        "header": "To ban user in every group where you are admin.",
        "الـوصـف": "Will ban the person in every group where you are admin only.",
        "الاستخـدام": "{tr}gban <username/reply/userid> <reason (optional)>",
    },
)
async def repgban(event):  # sourcery no-metrics
    "To ban user in every group where you are admin."
    repe = await edit_or_reply(event, "**╮ ❐... جـاࢪِ حـظـࢪ الشخـص عـام**")
    start = datetime.now()
    user, reason = await get_user_from_event(event, repe)
    if not user:
        return
    if user.id == zq_lo.uid:
        return await edit_delete(repe, "**⎉╎عـذراً ..لا استطيـع حظـࢪ نفسـي **")
    if user.id in rep_dev:
        return await edit_delete(repe, "**⎉╎عـذراً ..لا استطيـع حظـࢪ احـد المطـورين عـام **")
    if user.id == 925972505 or user.id == 5502537272 or user.id == 5502537272:
        return await edit_delete(repe, "**⎉╎عـذراً ..لا استطيـع حظـࢪ مطـور السـورس عـام **")


    if gban_sql.is_gbanned(user.id):
        await repe.edit(
            f"**⎉╎المسـتخـدم ↠** [{user.first_name}](tg://user?id={user.id}) \n**⎉╎مـوجــود بالفعــل فـي ↠ قائمـة المحظــورين عــام**"
        )
    else:
        gban_sql.repgban(user.id, reason)
    san = await admin_groups(event.client)
    count = 0
    sandy = len(san)
    if sandy == 0:
        return await edit_delete(repe, "**⎉╎عــذراً .. يجـب ان تكــون مشـرفـاً فـي مجموعـة واحـده ع الأقــل **")
    await repe.edit(
        f"**⎉╎جـاري بـدء حظـر ↠** [{user.first_name}](tg://user?id={user.id}) **\n\n**⎉╎مـن ↠ {len(san)} كــروب**"
    )
    for i in range(sandy):
        try:
            await event.client(EditBannedRequest(san[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            achat = await event.client.get_entity(san[i])
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**⎉╎عــذراً .. لـيس لـديــك صـلاحيـات فـي ↠**\n**⎉╎كــروب :** {get_display_name(achat)}(`{achat.id}`)",
            )
    end = datetime.now()
    reptaken = (end - start).seconds
    if reason:
        await repe.edit(
            f"**⎉╎المستخـدم :** [{user.first_name}](tg://user?id={user.id})\n\n**⎉╎تم حـظـࢪه عـام مـن {count} كــࢪوب خـلال {reptaken} ثـانيـه**\n**⎉╎السـبب :** {reason}"
        )
    else:
        await repe.edit(
            f"**╮ ❐... الشخـص :** [{user.first_name}](tg://user?id={user.id})\n\n**╮ ❐... تـم حـظـࢪه عـام مـن {count} كــࢪوب خـلال {reptaken} ثـانيـه**"
        )
    if BOTLOG and count != 0:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#الحظــࢪ_العـــام\
                \n**المعلـومـات :-**\
                \n**- الشخــص : **[{user.first_name}](tg://user?id={user.id})\
                \n**- الايــدي : **`{user.id}`\
                \n**- الســبب :** `{reason}`\
                \n**- تـم حظـره مـن**  {count}  **كــروب**\
                \n**- الــوقت المسـتغــࢪق :** {reptaken} **ثــانيـه**",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#الحظــࢪ_العـــام\
                \n**المعلـومـات :-**\
                \n**- الشخــص : **[{user.first_name}](tg://user?id={user.id})\
                \n**- الايــدي : **`{user.id}`\
                \n**- تـم حظـره مـن**  {count}  **كــروب**\
                \n**- الــوقت المسـتغــࢪق :** {reptaken} **ثــانيـه**",
            )
        with contextlib.suppress(BadRequestError):
            if reply:
                await reply.forward_to(BOTLOG_CHATID)
                await reply.delete()


@zq_lo.rep_cmd(
    pattern="الغاء ح عام(?:\s|$)([\s\S]*)",
    command=("الغاء ح عام", plugin_category),
    info={
        "header": "To unban the person from every group where you are admin.",
        "الـوصـف": "will unban and also remove from your gbanned list.",
        "الاستخـدام": "{tr}ungban <username/reply/userid>",
    },
)
async def repgban(event):
    "To unban the person from every group where you are admin."
    repe = await edit_or_reply(event, "**╮ ❐  جـاري الغــاء الحظـر العــام ❏╰**")
    start = datetime.now()
    user, reason = await get_user_from_event(event, repe)
    if not user:
        return
    if gban_sql.is_gbanned(user.id):
        gban_sql.catungban(user.id)
    else:
        return await edit_delete(
            repe,
            f"**⎉╎المسـتخـدم ↠** [{user.first_name}](tg://user?id={user.id}) **\n\n**⎉╎ليـس مـوجــود فـي ↠ قائمـة المحظــورين عــام**",
        )
    san = await admin_groups(event.client)
    count = 0
    sandy = len(san)
    if sandy == 0:
        return await edit_delete(zede, "**⎉╎عــذراً .. يجـب ان تكــون مشـرفـاً فـي مجموعـة واحـده ع الأقــل **")
    await repe.edit(
        f"**⎉╎جـاري الغــاء حظـر ↠** [{user.first_name}](tg://user?id={user.id}) **\n\n**⎉╎مـن ↠ {len(san)} كــروب**"
    )
    for i in range(sandy):
        try:
            await event.client(EditBannedRequest(san[i], user.id, UNBAN_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            achat = await event.client.get_entity(san[i])
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**⎉╎عــذراً .. لـيس لـديــك صـلاحيـات فـي ↠**\n**⎉╎كــروب :** {get_display_name(achat)}(`{achat.id}`)",
            )
    end = datetime.now()
    reptaken = (end - start).seconds
    if reason:
        await repe.edit(
            f"**⎉╎المستخـدم :** [{user.first_name}](tg://user?id={user.id})\n\n**⎉╎تم الغــاء حـظـࢪه عـام مـن {count} كــࢪوب خـلال {reptaken} ثـانيـه**\n**⎉╎السـبب :** {reason}"
        )
    else:
        await repe.edit(
            f"**⎉╎المستخـدم :** [{user.first_name}](tg://user?id={user.id})\n\n**⎉╎تم الغــاء حـظـࢪه عـام مـن {count} كــࢪوب خـلال {reptaken} ثـانيـه**"
        )

    if BOTLOG and count != 0:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#الغـــاء_الحظــࢪ_العـــام\
                \n**المعلـومـات :-**\
                \n**- الشخــص : **[{user.first_name}](tg://user?id={user.id})\
                \n**- الايــدي : **`{user.id}`\
                \n**- الســبب :** `{reason}`\
                \n**- تـم الغــاء حظـره مـن  {count} كــروب**\
                \n**- الــوقت المسـتغــࢪق :** {reptaken} **ثــانيـه**",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#الغـــاء_الحظــࢪ_العـــام\
                \n**المعلـومـات :-**\
                \n**- الشخــص : **[{user.first_name}](tg://user?id={user.id})\
                \n**- الايــدي : **`{user.id}`\
                \n**- تـم الغــاء حظـره مـن  {count} كــروب**\
                \n**- الــوقت المسـتغــࢪق :** {reptaken} **ثــانيـه**",
            )


@zq_lo.rep_cmd(
    pattern="العام$",
    command=("العام", plugin_category),
    info={
        "header": "Shows you the list of all gbanned users by you.",
        "الاستخـدام": "{tr}listgban",
    },
)
async def gablist(event):
    "Shows you the list of all gbanned users by you."
    gbanned_users = gban_sql.get_all_gbanned()
    GBANNED_LIST = "- قائمـة المحظـورين عــام :\n\n"
    if len(gbanned_users) > 0:
        for a_user in gbanned_users:
            if a_user.reason:
                GBANNED_LIST += f"**⎉╎المستخـدم :**  [{a_user.chat_id}](tg://user?id={a_user.chat_id}) \n**⎉╎سـبب الحظـر : {a_user.reason} ** \n\n"
            else:
                GBANNED_LIST += (
                    f"**⎉╎المستخـدم :**  [{a_user.chat_id}](tg://user?id={a_user.chat_id}) \n**⎉╎سـبب الحظـر : لا يـوجـد ** \n\n"
                )
    else:
        GBANNED_LIST = "**- لايــوجـد محظــورين عــام بعــد**"
    await edit_or_reply(event, GBANNED_LIST)


@zq_lo.rep_cmd(
    pattern="ط عام(?:\s|$)([\s\S]*)",
    command=("ط عام", plugin_category),
    info={
        "header": "kicks the person in all groups where you are admin.",
        "الاستخـدام": "{tr}gkick <username/reply/userid> <reason (optional)>",
    },
)
async def catgkick(event):  # sourcery no-metrics
    "kicks the person in all groups where you are admin"
    repe = await edit_or_reply(event, "**╮ ❐ ... جــاࢪِ طــرد الشخــص عــام ... ❏╰**")
    start = datetime.now()
    user, reason = await get_user_from_event(event, repe)
    if not user:
        return
    if user.id == zq_lo.uid:
        return await edit_delete(repe, "**╮ ❐ ... عــذراً لا استطــيع طــرد نفســي ... ❏╰**")
    if user.id in rep_dev:
        return await edit_delete(repe, "**╮ ❐ ... عــذࢪاً .. لا استطــيع طــرد المطـورين ... ❏╰**")
    if user.id == 5502537272 or user.id == 5502537272 or user.id == 5502537272:
        return await edit_delete(repe, "**╮ ❐ ... عــذࢪاً .. لا استطــيع طــرد مطـور السـورس ... ❏╰**")
    san = await admin_groups(event.client)
    count = 0
    sandy = len(san)
    if sandy == 0:
        return await edit_delete(repe, "**⎉╎عــذراً .. يجـب ان تكــون مشـرفـاً فـي مجموعـة واحـده ع الأقــل **")
    await zede.edit(
        f"**⎉╎بـدء طـرد ↠** [{user.first_name}](tg://user?id={user.id}) **\n\n**⎉╎فـي ↠ {len(san)} كــروب**"
    )
    for i in range(sandy):
        try:
            await event.client.kick_participant(san[i], user.id)
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            achat = await event.client.get_entity(san[i])
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**⎉╎عــذراً .. لـيس لـديــك صـلاحيـات فـي ↠**\n**⎉╎كــروب :** {get_display_name(achat)}(`{achat.id}`)",
            )
    end = datetime.now()
    reptaken = (end - start).seconds
    if reason:
        await repe.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was gkicked in {count} groups in {reptaken} seconds`!!\n**- الســبب :** `{reason}`"
        )
    else:
        await zede.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was gkicked in {count} groups in {reptaken} seconds`!!"
        )

    if BOTLOG and count != 0:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#الطــࢪد_العـــام\
                \n**المعلـومـات :-**\
                \n**- الشخــص : **[{user.first_name}](tg://user?id={user.id})\
                \n**- الايــدي : **`{user.id}`\
                \n**- الســبب :** `{reason}`\
                \n**- تـم طــرده مـن**  {count}  **كــروب**\
                \n**- الــوقت المسـتغــࢪق :** {reptaken} **ثــانيـه**",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#الطــࢪد_العـــام\
                \n**المعلـومـات :-**\
                \n**- الشخــص : **[{user.first_name}](tg://user?id={user.id})\
                \n**- الايــدي : **`{user.id}`\
                \n**- تـم طــرده مـن**  {count}  **كــروب**\
                \n**- الــوقت المسـتغــࢪق :** {reptaken} **ثــانيـه**",
            )
        if reply:
            await reply.forward_to(BOTLOG_CHATID)
