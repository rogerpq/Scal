import time
import asyncio
import importlib
import logging
import glob
import os
import sys
import urllib.request
from datetime import timedelta
from pathlib import Path
from random import randint
from datetime import datetime as dt
from pytz import timezone
import requests
import heroku3

from telethon import Button, functions, types, utils
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.contacts import UnblockRequest

from repthon import BOTLOG, BOTLOG_CHATID, PM_LOGGER_GROUP_ID

from ..Config import Config
from ..core.logger import logging
from ..core.session import zq_lo
from ..helpers.utils import install_pip
from ..helpers.utils.utils import runcmd
from ..sql_helper.global_collection import (
    del_keyword_collectionlist,
    get_item_collectionlist,
)
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from .pluginmanager import load_module
from .tools import create_supergroup

ENV = bool(os.environ.get("ENV", False))
LOGS = logging.getLogger("𝐑𝐞𝐩𝐭𝐡𝐨𝐧")
cmdhr = Config.COMMAND_HAND_LER
Rep_Vip = (5502537272)
Rep_Dev = (5502537272)
rchannel = {"@Repthon", "@Repthonn", "@Repthon_up", "@Repthon_vars", "@Repthon_support", "@Repthon_cklaish", "@ZQ_LO", "@xxfir", "@Repthon_help", "@roger21v", "@Devs_Repthon", "@Test_Repthon"}
heroku_api = "https://api.heroku.com"
if Config.HEROKU_APP_NAME is not None and Config.HEROKU_API_KEY is not None:
    Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
    app = Heroku.app(Config.HEROKU_APP_NAME)
    heroku_var = app.config()
else:
    app = None


if ENV:
    VPS_NOLOAD = ["vps"]
elif os.path.exists("config.py"):
    VPS_NOLOAD = ["heroku"]

bot = zq_lo
DEV = 5502537272


async def autovars(): #Code by T.me/E_7_V
    if "ENV" in heroku_var and "TZ" in heroku_var:
        return
    if "ENV" in heroku_var and "TZ" not in heroku_var:
        LOGS.info("جـارِ اضافـة بقيـة الفـارات .. تلقائيـاً")
        rrcom = "."
        rrrtz = "Asia/Baghdad"
        heroku_var["COMMAND_HAND_LER"] = rrcom
        heroku_var["TZ"] = rrrtz
        LOGS.info("تم اضافـة بقيـة الفـارات .. بنجـاح")
    if "ENV" not in heroku_var and "TZ" not in heroku_var:
        LOGS.info("جـارِ اضافـة بقيـة الفـارات .. تلقائيـاً")
        rrenv = "ANYTHING"
        rrcom = "."
        rrrtz = "Asia/Baghdad"
        heroku_var["ENV"] = rrenv
        heroku_var["COMMAND_HAND_LER"] = rrcom
        heroku_var["TZ"] = rrrtz
        LOGS.info("تم اضافـة بقيـة الفـارات .. بنجـاح")


async def autoname(): #Code by T.me/E_7_V
    if gvarstatus("ALIVE_NAME"):
        return
    await bot.start()
    await asyncio.sleep(15)
    LOGS.info("جـارِ اضافة فـار الاسـم التلقـائـي .. انتظـر قليـلاً")
    baqir = await bot.get_me()
    rrname = f"{baqir.first_name} {baqir.last_name}" if baqir.last_name else f"{baqir.first_name}"
    tz = Config.TZ
    tzDateTime = dt.now(timezone(tz))
    rdate = tzDateTime.strftime('%Y/%m/%d')
    militaryTime = tzDateTime.strftime('%H:%M')
    rtime = dt.strptime(militaryTime, "%H:%M").strftime("%I:%M %p")
    rrd = f"‹ {rdate} ›"
    rrt = f"‹ {rtime} ›"
    if gvarstatus("r_date") is None:
        rd = "r_date"
        rt = "r_time"
        rn = "ALIVE_NAME"
        addgvar(rd, rrd)
        addgvar(rt, rrt)
        addgvar(rn, rrname)
    LOGS.info(f"تم اضافـة اسـم المستخـدم {rrname} .. بنجـاح")


async def setup_bot():
    """
    To set up bot for Repthon
    """
    try:
        await zq_lo.connect()
        config = await zq_lo(functions.help.GetConfigRequest())
        for option in config.dc_options:
            if option.ip_address == zq_lo.session.server_address:
                if zq_lo.session.dc_id != option.id:
                    LOGS.warning(
                        f"ايـدي DC ثـابت فـي الجلسـة مـن {zq_lo.session.dc_id}"
                        f" الـى {option.id}"
                    )
                zq_lo.session.set_dc(option.id, option.ip_address, option.port)
                zq_lo.session.save()
                break
        details = await zq_lo.tgbot.get_me()
        Config.APP_USERNAME = f"@{details.username}"
        # await zq_lo.start(app_token=Config.APP_USERNAME)
        zq_lo.me = await zq_lo.get_me()
        zq_lo.uid = zq_lo.tgbot.uid = utils.get_peer_id(zq_lo.me)
        if Config.OWNER_ID == 0:
            Config.OWNER_ID = utils.get_peer_id(zq_lo.me)
    except Exception as e:
        LOGS.error(f"كـود تيرمكس - {str(e)}")
        sys.exit()


async def mybot(): #Code by T.me/E_7_V
    BAQIR = bot.me.first_name
    Taiba = bot.uid
    ba_qir = f"[{BAQIR}](tg://user?id={Taiba})"
    f"ـ {ba_qir}"
    f"•⎆┊هــذا البــوت خــاص بـ {ba_qir} يمكـنك التواصــل معـه هـنا 🧸♥️"
    babot = await zq_lo.tgbot.get_me()
    bot_name = babot.first_name
    botname = f"@{babot.username}"
    if bot_name.startswith("مسـاعـد"):
        print("تم تشغيل البوت بنجــاح")
    else:
        try:
            await bot.send_message("@BotFather", "/setinline")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "ريبـــثون")
            await asyncio.sleep(3)
            await bot.send_message("@BotFather", "/setname")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", f"مسـاعـد - {bot.me.first_name} ")
            await asyncio.sleep(3)
            await bot.send_message("@BotFather", "/setuserpic")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_file("@BotFather", "repthon/baqir/Repthon3.jpg")
            await asyncio.sleep(3)
            await bot.send_message("@BotFather", "/setabouttext")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", f"- بـوت ريبـــثون المسـاعـد ♥️🦾 الخـاص بـ  {bot.me.first_name}")
            await asyncio.sleep(3)
            await bot.send_message("@BotFather", "/setdescription")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", f"•⎆┊انـا البــوت المسـاعـد الخــاص بـ {ba_qir} \n•⎆┊بـواسطـتـي يمكـنك التواصــل مـع مـالكـي 🧸♥️\n•⎆┊قنـاة السـورس 🌐 @Repthon 🌐")
        except Exception as e:
            print(e)


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    if gvarstatus("PMLOG") and gvarstatus("PMLOG") != "false":
        delgvar("PMLOG")
    if gvarstatus("GRPLOG") and gvarstatus("GRPLOG") != "false":
        delgvar("GRPLOG")
    try:
        if BOTLOG:
            Config.ZQ_LOBLOGO = await zq_lo.tgbot.send_file(
                BOTLOG_CHATID,
                "https://graph.org/file/f367d5a4a6bf1fbfc99b9.mp4",
                caption="**•⎆┊تـم بـدء تشغـيل سـورس ريبـــثون الخاص بك .. بنجاح 🧸♥️**",
                buttons=[(Button.url("𝙍𝙀𝙋𝙏𝙃𝙊𝙉𓅛✓", "https://t.me/Repthon"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        msg_details = list(get_item_collectionlist("restart_update"))
        if msg_details:
            msg_details = msg_details[0]
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        if msg_details:
            await zq_lo.check_testcases()
            message = await zq_lo.get_messages(msg_details[0], ids=msg_details[1])
            text = message.text + "\n\n**•⎆┊تـم اعـادة تشغيـل السـورس بنجــاح 🧸♥️**"
            await zq_lo.edit_message(msg_details[0], msg_details[1], text)
            if gvarstatus("restartupdate") is not None:
                await zq_lo.send_message(
                    msg_details[0],
                    f"{cmdhr}بنك",
                    reply_to=msg_details[1],
                    schedule=timedelta(seconds=10),
                )
            del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
        return None


async def add_bot_to_logger_group(chat_id):
    """
    To add bot to logger groups
    """
    bot_details = await zq_lo.tgbot.get_me()
    try:
        await zq_lo(
            functions.messages.AddChatUserRequest(
                chat_id=chat_id,
                user_id=bot_details.username,
                fwd_limit=1000000,
            )
        )
    except BaseException:
        try:
            await zq_lo(
                functions.channels.InviteToChannelRequest(
                    channel=chat_id,
                    users=[bot_details.username],
                )
            )
        except Exception as e:
            LOGS.error(str(e))


async def saves():
   for Rcc in rchannel:
        try:
             await zq_lo(JoinChannelRequest(channel=Rcc))
        except OverflowError:
            LOGS.error("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
            continue


async def load_plugins(folder, extfolder=None):
    """
    To load plugins from the mentioned folder
    """
    if extfolder:
        path = f"{extfolder}/*.py"
        plugin_path = extfolder
    else:
        path = f"repthon/{folder}/*.py"
        plugin_path = f"repthon/{folder}"
    files = glob.glob(path)
    files.sort()
    success = 0
    failure = []
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            pluginname = shortname.replace(".py", "")
            try:
                if (pluginname not in Config.NO_LOAD) and (
                    pluginname not in VPS_NOLOAD
                ):
                    flag = True
                    check = 0
                    while flag:
                        try:
                            load_module(
                                pluginname,
                                plugin_path=plugin_path,
                            )
                            if shortname in failure:
                                failure.remove(shortname)
                            success += 1
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if shortname not in failure:
                                failure.append(shortname)
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"{plugin_path}/{shortname}.py"))
            except Exception as e:
                if shortname not in failure:
                    failure.append(shortname)
                os.remove(Path(f"{plugin_path}/{shortname}.py"))
                LOGS.info(
                    f"لا يمكنني تحميل {shortname} بسبب الخطأ {e}\nمجلد القاعده {plugin_path}"
                )
    if extfolder:
        if not failure:
            failure.append("None")
        await zq_lo.tgbot.send_message(
            BOTLOG_CHATID,
            f'Your external repo plugins have imported \n**No of imported plugins :** `{success}`\n**Failed plugins to import :** `{", ".join(failure)}`',
        )



async def verifyLoggerGroup():
    """
    Will verify the both loggers group
    """
    flag = False
    if BOTLOG:
        try:
            entity = await zq_lo.get_entity(BOTLOG_CHATID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "- الصلاحيات غير كافيه لأرسال الرسالئل في مجموعه فار ااـ PRIVATE_GROUP_BOT_API_ID."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "لا تمتلك صلاحيات اضافه اعضاء في مجموعة فار الـ PRIVATE_GROUP_BOT_API_ID."
                    )
        except ValueError:
            LOGS.error(
                "PRIVATE_GROUP_BOT_API_ID لم يتم العثور عليه . يجب التاكد من ان الفار صحيح."
            )
        except TypeError:
            LOGS.error(
                "PRIVATE_GROUP_BOT_API_ID قيمه هذا الفار غير مدعومه. تأكد من انه صحيح."
            )
        except Exception as e:
            LOGS.error(
                "حدث خطأ عند محاولة التحقق من فار PRIVATE_GROUP_BOT_API_ID.\n"
                + str(e)
            )
    else:
        descript = "لا تقم بحذف هذه المجموعة أو التغيير إلى مجموعة عامه (وظيفتهـا تخزيـن كـل سجـلات وعمليـات البـوت.)"
        photozed = await zq_lo.upload_file(file="baqir/taiba/Repthon1.jpg")
        _, groupid = await create_supergroup(
            "كـروب السجـل ريبـــثون", zq_lo, Config.APP_USERNAME, descript, photozed
        )
        addgvar("PRIVATE_GROUP_BOT_API_ID", groupid)
        print("تم إنشاء مجموعة السجل .. بنجاح ✅")
        flag = True
    if PM_LOGGER_GROUP_ID != -100:
        try:
            entity = await zq_lo.get_entity(PM_LOGGER_GROUP_ID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        " الصلاحيات غير كافيه لأرسال الرسالئل في مجموعه فار ااـ PM_LOGGER_GROUP_ID."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "لا تمتلك صلاحيات اضافه اعضاء في مجموعة فار الـ  PM_LOGGER_GROUP_ID."
                    )
        except ValueError:
            LOGS.error("PM_LOGGER_GROUP_ID لم يتم العثور على قيمه هذا الفار . تاكد من أنه صحيح .")
        except TypeError:
            LOGS.error("PM_LOGGER_GROUP_ID قيمه هذا الفار خطا. تاكد من أنه صحيح.")
        except Exception as e:
            LOGS.error("حدث خطأ اثناء التعرف على فار PM_LOGGER_GROUP_ID.\n" + str(e))
    else:
        descript = "لا تقم بحذف هذه المجموعة أو التغيير إلى مجموعة عامه (وظيفتهـا تخزيـن رسـائل الخـاص.)"
        photozed = await zq_lo.upload_file(file="baqir/taiba/Repthon2.jpg")
        _, groupid = await create_supergroup(
            "مجمـوعـة التخـزيـن", zq_lo, Config.APP_USERNAME, descript, photozed
        )
        addgvar("PM_LOGGER_GROUP_ID", groupid)
        print("تم إنشاء مجموعة التخزين .. بنجاح ✅")
        flag = True
    if flag:
        executable = sys.executable.replace(" ", "\\ ")
        args = [executable, "-m", "repthon"]
        os.execle(executable, *args, os.environ)
        sys.exit(0)


async def install_externalrepo(repo, branch, cfolder):
    repREPO = repo
    rpath = os.path.join(cfolder, "requirements.txt")
    if repBRANCH := branch:
        repourl = os.path.join(repREPO, f"tree/{repBRANCH}")
        gcmd = f"git clone -b {repBRANCH} {repREPO} {cfolder}"
        errtext = f"There is no branch with name `{repBRANCH}` in your external repo {repREPO}. Recheck branch name and correct it in vars(`EXTERNAL_REPO_BRANCH`)"
    else:
        repourl = repREPO
        gcmd = f"git clone {repREPO} {cfolder}"
        errtext = f"The link({repREPO}) you provided for `EXTERNAL_REPO` in vars is invalid. please recheck that link"
    response = urllib.request.urlopen(repourl)
    if response.code != 200:
        LOGS.error(errtext)
        return await zq_lo.tgbot.send_message(BOTLOG_CHATID, errtext)
    await runcmd(gcmd)
    if not os.path.exists(cfolder):
        LOGS.error(
            "- حدث خطأ اثناء استدعاء رابط الملفات الاضافية .. قم بالتأكد من الرابط اولاً..."
        )
        return await zq_lo.tgbot.send_message(
            BOTLOG_CHATID,
            "**- حدث خطأ اثناء استدعاء رابط الملفات الاضافية .. قم بالتأكد من الرابط اولاً...**",
        )
    if os.path.exists(rpath):
        await runcmd(f"pip3 install --no-cache-dir -r {rpath}")
    await load_plugins(folder="repthon", extfolder=cfolder)
