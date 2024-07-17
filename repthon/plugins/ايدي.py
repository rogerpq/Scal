import asyncio
import contextlib
import re
import html
import shutil
import os
import base64
import requests
from requests import get

from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import MessageEntityMentionName
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import pack_bot_file_id
from telethon.errors.rpcerrorlist import YouBlockedUserError, ChatSendMediaForbiddenError

from . import zq_lo
from ..Config import Config
from ..utils import Rep_Vip
from ..helpers import reply_id
from ..helpers.utils import _format
from ..core.logger import logging
from ..core.managers import edit_or_reply, edit_delete
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..sql_helper.echo_sql import addecho, get_all_echos, get_echos, is_echo, remove_all_echos, remove_echo, remove_echos
from . import BOTLOG, BOTLOG_CHATID, spamwatch

plugin_category = "utils"
LOGS = logging.getLogger(__name__)
# @E_7_V
r_dev = (6583951825, 5895554306, 9848752505, 528089206, 54281890871, 5895554306)
rep_dev = (1260465030, 1960777228, 1145818344)
baqir = (5502537272, 5502537272, 5502537272)
RID = gvarstatus("R_ID") or "ايديه"
Rep_Uid = zq_lo.uid

REP_BLACKLIST = [
    -1001526282589,
    ]

async def get_user_from_event(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_object = await event.client.get_entity(previous_message.sender_id)
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if not user:
            self_user = await event.client.get_me()
            user = self_user.id
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        if isinstance(user, int) or user.startswith("@"):
            user_obj = await event.client.get_entity(user)
            return user_obj
        try:
            user_object = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_object


async def fetch_baqir(user_id):
    headers = {
        'Host': 'restore-access.indream.app',
        'Connection': 'keep-alive',
        'x-api-key': 'e758fb28-79be-4d1c-af6b-066633ded128',
        'Accept': '*/*',
        'Accept-Language': 'ar',
        'Content-Length': '25',
        'User-Agent': 'Nicegram/101 CFNetwork/1404.0.5 Darwin/22.3.0',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = '{"telegramId":' + str(user_id) + '}'
    response = requests.post('https://restore-access.indream.app/regdate', headers=headers, data=data).json()
    baqir_date = response['data']['date']
    return baqir_date


async def rrr_info(repthon_user, event):
    FullUser = (await event.client(GetFullUserRequest(repthon_user.id))).full_user
    first_name = repthon_user.first_name
    full_name = FullUser.private_forward_name
    user_id = repthon_user.id
    baqir_sinc = await fetch_baqir(user_id)
    username = repthon_user.username
    verified = repthon_user.verified
    r = (await event.client.get_entity(user_id)).premium
    first_name = (
        first_name.replace("\u2060", "")
        if first_name
        else ("هذا المستخدم ليس له اسم أول")
    )
    full_name = full_name or first_name
    username = "@{}".format(username) if username else ("لا يـوجـد")
    rrrsinc = baqir_sinc if baqir_sinc else ("غيـر معلـوم")
################# Dev Baqir #################
    Repthon = f'<a href="T.me/Repthon">ᯓ 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗗𝗮𝘁𝗮 📟</a>'
    Repthon += f"\n<b>⋆─┄─┄─┄─┄─┄─┄─⋆</b>\n\n"
    Repthon += f"<b>• معلومـات إنشـاء حسـاب تيليجـرام 📑 :</b>\n"
    Repthon += f"<b>- الاسـم    ⤎ </b> "
    Repthon += f'<a href="tg://user?id={user_id}">{full_name}</a>'
    Repthon += f"\n<b>- الايــدي   ⤎ </b> <code>{user_id}</code>"
    Repthon += f"\n<b>- اليـوزر    ⤎  {username}</b>\n"
    if r == True or user_id in baqir: 
        Repthon += f"<b>- الحساب  ⤎  بـريميـوم 🌟</b>\n"
    Repthon += f"<b>- الإنشـاء   ⤎</b>  {rrrsinc}  🗓" 
    return Repthon

async def fetch_info(replied_user, event):
    """Get details from the User object."""
    FullUser = (await event.client(GetFullUserRequest(replied_user.id))).full_user
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(user_id=replied_user.id, offset=42, max_id=0, limit=80)
    )
    replied_user_profile_photos_count = "لا يـوجـد بروفـايـل"
    dc_id = "Can't get dc id"
    with contextlib.suppress(AttributeError):
        replied_user_profile_photos_count = replied_user_profile_photos.count
        dc_id = replied_user.photo.dc_id
    user_id = replied_user.id
    baqir_sinc = await fetch_baqir(user_id)
    first_name = replied_user.first_name
    full_name = FullUser.private_forward_name
    common_chat = FullUser.common_chats_count
    username = replied_user.username
    user_bio = FullUser.about
    is_bot = replied_user.bot
    restricted = replied_user.restricted
    verified = replied_user.verified
    r = (await event.client.get_entity(user_id)).premium
    if r == True or user_id in baqir: 
        rpre = "ℙℝ𝔼𝕄𝕀𝕌𝕄 🌟"
    else:
        rpre = "𝕍𝕀ℝ𝕋𝕌𝔸𝕃 ✨"
    if user_id in Rep_Vip: 
        rvip = "𝕍𝕀ℙ 💎"
    else:
        rvip = "ℕ𝕆ℕ𝔼"
    photo = await event.client.download_profile_photo(
        user_id,
        Config.TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg",
        download_big=True,
    )
    first_name = (
        first_name.replace("\u2060", "")
        if first_name
        else ("هذا المستخدم ليس له اسم أول")
    )
    full_name = full_name or first_name
    username = "@{}".format(username) if username else ("لا يـوجـد")
    user_bio = "لا يـوجـد" if not user_bio else user_bio
    rrrsinc = baqir_sinc if baqir_sinc else ("غيـر معلـوم")
    rmsg = await bot.get_messages(event.chat_id, 0, from_user=user_id) 
    rrr = rmsg.total
    if rrr < 100: 
        baqr = "غير متفاعل  🗿"
    elif rrr > 200 and rrr < 500:
        baqr = "ضعيف  🗿"
    elif rrr > 500 and rrr < 700:
        baqr = "شد حيلك  🏇"
    elif rrr > 700 and rrr < 1000:
        baqr = "ماشي الحال  🏄🏻‍♂"
    elif rrr > 1000 and rrr < 2000:
        baqr = "ملك التفاعل  🎖"
    elif rrr > 2000 and rrr < 3000:
        baqr = "امبراطور التفاعل  🥇"
    elif rrr > 3000 and rrr < 4000:
        baqr = "غنبله  💣"
    else:
        baqr = "نار وشرر  🏆"
################# Dev Baqir #################
    if user_id in baqir: 
        rotbat = "مطـور السـورس 𓄂" 
    elif user_id in rep_dev:
        rotbat = "مـطـور 𐏕" 
    elif user_id == (await event.client.get_me()).id and user_id not in r_dev:
        rotbat = "مـالك الحساب 𓀫" 
    else:
        rotbat = "العضـو 𓅫"
################# Dev Baqir #################
    REP_TEXT = gvarstatus("CUSTOM_ALIVE_TEXT") or "•⎚• مـعلومـات المسـتخـدم مـن بـوت ريبـــثون"  
    REPM = gvarstatus("CUSTOM_ALIVE_EMOJI") or "✦ " 
    REPF = gvarstatus("CUSTOM_ALIVE_FONT") or "ٴ⋆─┄─┄─┄─ ᴿᴱᴾᵀᴴᴼᴺ ─┄─┄─┄─⋆" 
    if gvarstatus("RID_TEMPLATE") is None:
        caption = f"<b> {REP_TEXT} </b>\n"
        caption += f"ٴ<b>{REPF}</b>\n"
        caption += f"<b>{REPM}الاســم        ⤎ </b> "
        caption += f'<a href="tg://user?id={user_id}">{full_name}</a>'
        caption += f"\n<b>{REPM}اليـوزر        ⤎  {username}</b>"
        caption += f"\n<b>{REPM}الايـدي        ⤎ </b> <code>{user_id}</code>\n"
        caption += f"<b>{REPM}الرتبــه        ⤎ {rotbat} </b>\n" 
        if r == True or user_id in baqir: 
            caption += f"<b>{REPM}الحساب  ⤎  بـريميـوم 🌟</b>\n"
        if user_id in Rep_Vip: 
            caption += f"<b>{REPM}الاشتراك  ⤎  𝕍𝕀ℙ 💎</b>\n"
        caption += f"<b>{REPM}الصـور        ⤎</b>  {replied_user_profile_photos_count}\n"
        caption += f"<b>{REPM}الرسائل  ⤎</b>  {rrr}  💌\n" 
        caption += f"<b>{REPM}التفاعل  ⤎</b>  {baqr}\n" 
        if user_id != (await event.client.get_me()).id: 
            caption += f"<b>{REPM}الـمجموعات المشتـركة ⤎  {common_chat}</b>\n"
        caption += f"<b>{REPM}الإنشـاء  ⤎</b>  {rrrsinc}  🗓\n" 
        caption += f"<b>{REPM}البايـو         ⤎  {user_bio}</b>\n"
        caption += f"ٴ<b>{REPF}</b>"
    else:
        rrr_caption = gvarstatus("RID_TEMPLATE")
        caption = rrr_caption.format(
            rnam=full_name,
            rusr=username,
            ridd=user_id,
            rrtb=rotbat,
            rpre=rpre,
            rvip=rvip,
            rpic=replied_user_profile_photos_count,
            rmsg=rrr,
            rtmg=baqr,
            rcom=common_chat,
            rsnc=rrrsinc,
            rbio=user_bio,
        )
    return photo, caption


@zq_lo.rep_cmd(
    pattern="ايدي(?: |$)(.*)",
    command=("ايدي", plugin_category),
    info={
        "header": "لـ عـرض معلومـات الشخـص",
        "الاستـخـدام": " {tr}ايدي بالـرد او {tr}ايدي + معـرف/ايـدي الشخص",
    },
)
async def who(event):
    "Gets info of an user"
    if (event.chat_id in REP_BLACKLIST) and (Rep_Uid not in Rep_Vip):
        return await edit_or_reply(event, "**- عـذرًا .. عـزيـزي 🚷\n- لا تستطيـع استخـدام هـذا الأمـر 🚫\n- فـي مجموعـة مساعدة ريبـــثون ؟!**")
    rep = await edit_or_reply(event, "⇆")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user_from_event(event)
    try:
        photo, caption = await fetch_info(replied_user, event)
    except (AttributeError, TypeError):
        return await edit_or_reply(rep, "**- لـم استطـع العثــور ع الشخــص ؟!**")
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    if gvarstatus("RID_TEMPLATE") is None:
        try:
            await event.client.send_file(
                event.chat_id,
                photo,
                caption=caption,
                link_preview=False,
                force_document=False,
                reply_to=message_id_to_reply,
                parse_mode="html",
            )
            if not photo.startswith("http"):
                os.remove(photo)
            await rep.delete()
        except (TypeError, ChatSendMediaForbiddenError):
            await rep.edit(caption, parse_mode="html")
    else:
        try:
            await event.client.send_file(
                event.chat_id,
                photo,
                caption=caption,
                link_preview=False,
                force_document=False,
                reply_to=message_id_to_reply,
                parse_mode="md",
            )
            if not photo.startswith("http"):
                os.remove(photo)
            await rep.delete()
        except (TypeError, ChatSendMediaForbiddenError):
            await rep.edit(caption, parse_mode="md")


@zq_lo.rep_cmd(
    pattern="ا(?: |$)(.*)",
    command=("ا", plugin_category),
    info={
        "header": "امـر مختصـر لـ عـرض معلومـات الشخـص",
        "الاستـخـدام": " {tr}ا بالـرد او {tr}ا + معـرف/ايـدي الشخص",
    },
)
async def who(event):
    "Gets info of an user"
    if (event.chat_id in REP_BLACKLIST) and (Rep_Uid not in Rep_Vip):
        return await edit_or_reply(event, "**- عـذرًا .. عـزيـزي 🚷\n- لا تستطيـع استخـدام هـذا الأمـر 🚫\n- فـي مجموعـة مساعدة ريبـــثون ؟!**")
    rep = await edit_or_reply(event, "⇆")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user_from_event(event)
    try:
        photo, caption = await fetch_info(replied_user, event)
    except (AttributeError, TypeError):
        return await edit_or_reply(rep, "**- لـم استطـع العثــور ع الشخــص ؟!**")
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    if gvarstatus("RID_TEMPLATE") is None:
        try:
            await event.client.send_file(
                event.chat_id,
                photo,
                caption=caption,
                link_preview=False,
                force_document=False,
                reply_to=message_id_to_reply,
                parse_mode="html",
            )
            if not photo.startswith("http"):
                os.remove(photo)
            await rep.delete()
        except (TypeError, ChatSendMediaForbiddenError):
            await rep.edit(caption, parse_mode="html")
    else:
        try:
            await event.client.send_file(
                event.chat_id,
                photo,
                caption=caption,
                link_preview=False,
                force_document=False,
                reply_to=message_id_to_reply,
                parse_mode="md",
            )
            if not photo.startswith("http"):
                os.remove(photo)
            await rep.delete()
        except (TypeError, ChatSendMediaForbiddenError):
            await rep.edit(caption, parse_mode="md")


@zq_lo.rep_cmd(pattern="الانشاء(?: |$)(.*)")
async def baqir(event):
    rep = await edit_or_reply(event, "**- جـارِ جلب المعلومـات . . .**")
    repthon_user = await get_user_from_event(event)
    try:
        Repthon = await rrr_info(repthon_user, event)
    except (AttributeError, TypeError):
        return await edit_or_reply(rep, "**- لـم استطـع العثــور ع الشخــص ؟!**")
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_message(
            event.chat_id,
            Repthon,
            link_preview=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
        await rep.delete()
    except:
        await rep.edit("**- غيـر معلـوم او هنـاك خطـأ ؟!**", parse_mode="html")


@zq_lo.rep_cmd(pattern=f"{RID}(?: |$)(.*)")
async def hwo(event):
    if {event.chat_id in REP_BLACKLIST} and {Rep_Uid not in Rep_Vip}:
        return await edit_or_reply(event, "**- عـذرًا .. عـزيـزي 🚷\n- لا تستطيـع استخـدام هـذا الأمـر 🚫\n- فـي مجموعـة مساعدة ريبـــثون ؟!**")
    rep = await edit_or_reply(event, "⇆")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user_from_event(event)
    try:
        photo, caption = await fetch_info(replied_user, event)
    except (AttributeError, TypeError):
        return await edit_or_reply(rep, "**- لـم استطـع العثــور ع الشخــص ؟!**")
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
        if not photo.startswith("http"):
            os.remove(photo)
        await rep.delete()
    except TypeError:
        await rep.edit(caption, parse_mode="html")


@zq_lo.rep_cmd(
    pattern="صورته(?:\\s|$)([\\s\\S]*)",
    command=("صورته", plugin_category),
    info={
        "header": "لـ جـلب بـروفـايـلات الشخـص",
        "الاستـخـدام": [
            "{tr}صورته + عدد",
            "{tr}صورته الكل",
            "{tr}صورته",
        ],
    },
)
async def potocmd(event):
    "To get user or group profile pic"
    if (event.chat_id in REP_BLACKLIST) and (Rep_Uid not in Rep_Vip):
        return await edit_or_reply(event, "**- عـذرًا .. عـزيـزي 🚷\n- لا تستطيـع استخـدام هـذا الأمـر 🚫\n- فـي مجموعـة مساعدة ريبـــثون ؟!**")
    uid = "".join(event.raw_text.split(maxsplit=1)[1:])
    user = await event.get_reply_message()
    chat = event.input_chat
    if user and user.sender:
        photos = await event.client.get_profile_photos(user.sender)
        u = True
    else:
        photos = await event.client.get_profile_photos(chat)
        u = False
    if uid.strip() == "":
        uid = 1
        if int(uid) > (len(photos)):
            return await edit_delete(
                event, "**- لا يـوجـد هنـاك صـور لهـذا الشخـص ؟! **"
            )
        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    elif uid.strip() == "الكل":
        if len(photos) > 0:
            await event.client.send_file(event.chat_id, photos)
        else:
            try:
                if u:
                    photo = await event.client.download_profile_photo(user.sender)
                else:
                    photo = await event.client.download_profile_photo(event.input_chat)
                await event.client.send_file(event.chat_id, photo)
            except Exception:
                return await edit_delete(event, "**- لا يـوجـد هنـاك صـور لهـذا الشخـص ؟! **")
    else:
        try:
            uid = int(uid)
            if uid <= 0:
                await edit_or_reply(
                    event, "**- رقـم خـاطـئ . . .**"
                )
                return
        except BaseException:
            await edit_or_reply(event, "**- رقـم خـاطـئ . . .**")
            return
        if int(uid) > (len(photos)):
            return await edit_delete(
                event, "**- لا يـوجـد هنـاك صـور لهـذا الشخـص ؟! **"
            )

        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    await event.delete()


@zq_lo.rep_cmd(
    pattern="(الايدي|id)(?:\\s|$)([\\s\\S]*)",
    command=("id", plugin_category),
    info={
        "header": "To get id of the group or user.",
        "description": "if given input then shows id of that given chat/channel/user else if you reply to user then shows id of the replied user \
    along with current chat id and if not replied to user or given input then just show id of the chat where you used the command",
        "usage": "{tr}id <reply/username>",
    },
)
async def _(event):
    "To get id of the group or user."
    if input_str := event.pattern_match.group(2):
        try:
            p = await event.client.get_entity(input_str)
        except Exception as e:
            return await edit_delete(event, f"`{e}`", 5)
        try:
            if p.first_name:
                return await edit_or_reply(
                    event, f"**⎉╎أيدي المستخـدم**  `{input_str}` **هـو** `{p.id}`"
                )
        except Exception:
            try:
                if p.title:
                    return await edit_or_reply(
                        event, f"**⎉╎أيدي المستخـدم**  `{p.title}` **هـو** `{p.id}`"
                    )
            except Exception as e:
                LOGS.info(str(e))
        await edit_or_reply(event, "**⎉╎أدخل إما اسم مستخدم أو الرد على المستخدم**")
    elif event.reply_to_msg_id:
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await edit_or_reply(
                event,
                f"**⎉╎أيـدي الدردشـة : **`{event.chat_id}`\n\n**⎉╎أيـدي المستخـدم : **`{r_msg.sender_id}`\n\n**⎉╎ايـدي الميديـا : **`{bot_api_file_id}`",
            )

        else:
            await edit_or_reply(
                event,
                f"**⎉╎أيـدي الدردشـة : **`{event.chat_id}`\n\n**⎉╎أيـدي المستخـدم : **`{r_msg.sender_id}`",
            )

    else:
        await edit_or_reply(event, f"**⎉╎ايـدي الدردشـه : **`{event.chat_id}`")


@zq_lo.rep_cmd(
    pattern="رابطه(?:\\s|$)([\\s\\S]*)",
    command=("رابطه", plugin_category),
    info={
        "header": "لـ جـلب اسـم الشخـص بشكـل ماركـدون ⦇.رابطه بالـرد او + معـرف/ايـدي الشخص⦈ ",
        "الاسـتخـدام": "{tr}رابطه <username/userid/reply>",
    },
)
async def permalink(event):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(event)
    if not user:
        return
    if custom:
        return await edit_or_reply(event, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(event, f"[{tag}](tg://user?id={user.id})")


@zq_lo.rep_cmd(pattern="اسمي$")
async def permalink(event):
    user = await event.client.get_me()
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(event, f"[{tag}](tg://user?id={user.id})")


@zq_lo.rep_cmd(
    pattern="اسمه(?:\\s|$)([\\s\\S]*)",
    command=("اسمه", plugin_category),
    info={
        "header": "لـ جـلب اسـم الشخـص بشكـل ماركـدون ⦇.اسمه بالـرد او + معـرف/ايـدي الشخص⦈ ",
        "الاسـتخـدام": "{tr}اسمه <username/userid/reply>",
    },
)
async def permalink(event):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(event)
    if not user:
        return
    if custom:
        return await edit_or_reply(event, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(event, f"[{tag}](tg://user?id={user.id})")


@zq_lo.rep_cmd(pattern="الصور(?:\\s|$)([\\s\\S]*)")
async def potocmd(event):
    uid = "".join(event.raw_text.split(maxsplit=1)[1:])
    user = await get_user_from_event(event)
    rser = await event.get_reply_message()
    chat = event.input_chat
    if rser and ser.sender:
        photos = await event.client.get_profile_photos(rser.sender)
    else:
        photos = await event.client.get_profile_photos(user.id)
    if uid.strip() == "":
        if len(photos) > 0:
            await event.client.send_file(event.chat_id, photos)
        else:
            try:
                if rser:
                    photo = await event.client.download_profile_photo(rser.sender)
                else:
                    photo = await event.client.download_profile_photo(event.input_chat)
                await event.client.send_file(event.chat_id, photo)
            except Exception:
                return await edit_delete(event, "**- لا يـوجـد هنـاك صـور لهـذا الشخـص ؟! **")
    else:
        if len(photos) > 0:
            await event.client.send_file(event.chat_id, photos)
        else:
            try:
                photo = await event.client.download_profile_photo(user.id)
                await event.client.send_file(event.chat_id, photo)
            except Exception:
                return await edit_delete(event, "- لا يـوجـد هنـاك صـور لهـذا الشخـص ؟! ")
    await event.delete()


@zq_lo.rep_cmd(pattern="حساب(?: |$)(.*)")
async def openacc(event):
    acc = event.pattern_match.group(1)
    if not acc:
        return await edit_or_reply(event, "**- أرسـل الأمـر والايـدي فقـط**")
    rrr = await edit_or_reply(event, "**⎉╎جـارِ صنـع رابـط دخـول لـ الحسـاب ▬▭ ...**")
    caption=f"**- رابـط صاحب الايدي ( {acc} )** :\n**- الرابـط ينفتـح عبـر تطبيـق تيليكرام بلاس فقـط**\n\n[اضـغـط هـنـا](tg://openmessage?user_id={acc})"
    await edit_or_reply(event, caption)
