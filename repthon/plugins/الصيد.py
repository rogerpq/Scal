# by: t.me/Dar4k  ~ t.me/R0R77 ~ t.me/E_7_V

import random

import requests
import telethon
from fake_useragent import UserAgent
from telethon.sync import functions

from repthon import zq_lo

a = "qwertyuiopassdfghjklzxcvbnm"
b = "1234567890"
e = "qwertyuiopassdfghjklzxcvbnm1234567890"

trys, trys2 = [0], [0]
isclaim = ["off"]
isauto = ["off"]


def check_user(username):
    url = "https://t.me/" + str(username)
    ua = UserAgent()
    headers = {
        "User-Agent": ua.random,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    session = requests.Session()
    response = session.get(url, headers=headers)

    if (
        response.text.find(
            'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'
        )
        >= 0
    ):
        return True
    else:
        return False


def gen_user(choice):
    if choice == "ثلاثي":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = "".join(f)

    elif choice == "خماسي":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "خماسي حرفين":
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سداسي":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سداسي حرفين":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سباعي":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "بوتات":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], s[0], d[0]]
        username = "".join(f)
        username = username + "bot"

    elif choice == "تيست":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], d[0], d[0], c[0], c[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
    else:
        raise ValueError("Invalid choice for username generation.")
    return username


@zq_lo.rep_cmd(pattern="الصيد")
async def _(event):
    await event.edit(
        """
**أوامـر الـصـيـد الخـاصة بــســورس ريبـــثون**: 

ٴ— — — — — — — — — —

النوع :(  سداسي حرفين/ ثلاثي/ سداسي/ بوتات/ خماسي حرفين/خماسي /سباعي )

الامر:  `.صيد` + النوع
- يقوم بصيد معرفات عشوائية حسب النوع

الامر:  `تثبيت` + معرف
* وظيفة الامر : يقوم بالتثبيت على المعرف عندما يصبح متاح يأخذه

ٴ— — — — — — — — — —
الامر:   `.حالة الصيد`
• لمعرفة عدد المحاولات للصيد

الامر:  `.حالة التثبيت`
• لمعرفة عدد المحاولات للصيد

**@Repthon - channle userbot**

"""
    )


@zq_lo.rep_cmd(pattern="صيد (.*)")
async def hunterusername(event):
    choice = str(event.pattern_match.group(1))
    await event.edit(f"**- تم تفعيل الصيد بنجاح الان**")
    try:
        ch = await zq_lo(
            functions.channels.CreateChannelRequest(
                title="REPTHON HUNTER - صيد ريبثون",
                about="This channel to hunt username by - @Repthon",
            )
        )
        ch = ch.updates[1].channel_id
    except Exception as e:
        await zq_lo.send_message(
            event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**"
        )
        sedmod = False

    isclaim.clear()
    isclaim.append("on")
    sedmod = True
    while sedmod:
        username = gen_user(choice)
        if username == "error":
            await event.edit("**- يرجى وضع النوع بشكل صحيح**")
            break
        isav = check_user(username)
        if isav == True:
            try:
                await zq_lo(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_file(
                    event.chat_id,
                    "https://t.me/Repthongif/2",
                    caption="🐊 Repthon the best 🐊\n- - - - - - - - - - - - - - - - - - - - - - - -\n- UserName: ❲ @{} ❳\n- ClickS: ❲ {} ❳\n- Type: {}\n- Save: ❲ Chaneel ❳\n- - - - - - - - - - - - - - - - - - - - - - - -\nThE KiNgS ❲ @Repthon - @E_7_V ❳ ".format(
                        username, trys, choice
                    ),
                )
                await event.client.send_file(
                    ch,
                    "https://t.me/Repthongif/2",
                    caption="🐊 Repthon the best 🐊\n- - - - - - - - - - - - - - - - - - - - - - - -\n- UserName: ❲ @{} ❳\n- ClickS: ❲ {} ❳\n- Type: {}\n- Save: ❲ Chaneel ❳\n- - - - - - - - - - - - - - - - - - - - - - - -\nThE KiNgS ❲ @Repthon - @E_7_V ❳ ".format(
                        username, trys, choice
                    ),
                )
                await event.client.send_message(
                    "@E_7_V", f"- Done : @{username} !\n- By : @E_7_V - @Repthon !"
                )
                sedmod = False
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                pass
            except Exception as baned:
                if "(caused by UpdateUsernameRequest)" in str(baned):
                    pass
            except telethon.errors.FloodError as e:
                await zq_lo.send_message(
                    event.chat_id,
                    f"للاسف تبندت , مدة الباند**-  ({e.seconds}) ثانية .**",
                )
                sedmod = False
                break
            except Exception as eee:
                if "the username is already" in str(eee):
                    pass
                if "USERNAME_PURCHASE_AVAILABLE" in str(eee):
                    pass
                else:
                    await zq_lo.send_message(
                        event.chat_id,
                        f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",
                    )
                    sedmod = False
                    break
        else:
            pass
        trys[0] += 1
    isclaim.clear()
    isclaim.append("off")


@zq_lo.rep_cmd(pattern="تثبيت (.*)")
async def _(event):
    msg = event.text.split()
    try:
        ch = str(msg[2])
        ch = ch.replace("@", "")
        await event.edit(f"حسناً سيتم بدء التثبيت في**-  @{ch} .**")
    except:
        try:
            ch = await zq_lo(
                functions.channels.CreateChannelRequest(
                    title="REPTHON HUNTER - تثبيت ريبثون",
                    about="This channel to hunt username by - @Repthon",
                )
            )
            ch = ch.updates[1].channel_id
            await event.edit(f"**- تم بنجاح بدأ التثبيت**")
        except Exception as e:
            await zq_lo.send_message(
                event.chat_id, f"خطأ في انشاء القناة , الخطأ : {str(e)}"
            )
    isauto.clear()
    isauto.append("on")
    username = str(msg[1])

    swapmod = True
    while swapmod:
        isav = check_user(username)
        if isav == True:
            try:
                await zq_lo(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_file(
                    ch,
                    "https://t.me/Repthongif/2",
                    caption="🐊 Repthon the best 🐊\n- - - - - - - - - - - - - - - - - - - - - - - -\n- UserName: ❲ @{} ❳\n- ClickS: ❲ {} ❳\n- Save: ❲ Chaneel ❳\n- - - - - - - - - - - - - - - - - - - - - - - -\nThE KiNgS ❲ @Repthon - @E_7_V ❳ ".format(
                        username, trys2
                    ),
                )
                await event.client.send_file(
                    event.chat_id,
                    "https://t.me/Repthongif/2",
                    caption="🐊 Repthon the best 🐊\n- - - - - - - - - - - - - - - - - - - - - - - -\n- UserName: ❲ @{} ❳\n- ClickS: ❲ {} ❳\n- Save: ❲ Chaneel ❳\n- - - - - - - - - - - - - - - - - - - - - - - -\nThE KiNgS ❲ @Repthon - @E_7_V ❳ ".format(
                        username, trys2
                    ),
                )
                await event.client.send_message(
                    "@E_7_V",
                    f"- Done : @{username} !\n- By : @E_7_V - @Repthon!\n- Hunting Log {trys2}",
                )
                swapmod = False
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(
                    event.chat_id, f"المعرف **-  @{username} غير صالح . **"
                )
                swapmod = False
                break
            except telethon.errors.FloodError as e:
                await zq_lo.send_message(
                    event.chat_id, f"للاسف تبندت , مدة الباند ({e.seconds}) ثانية ."
                )
                swapmod = False
                break
            except Exception as eee:
                await zq_lo.send_message(
                    event.chat_id,
                    f"""خطأ مع {username} , الخطأ :{str(eee)}""",
                )
                swapmod = False
                break
        else:
            pass
        trys2[0] += 1

    isclaim.clear()
    isclaim.append("off")


@zq_lo.rep_cmd(pattern="ايقاف الصيد")
async def _(event):
    if "on" in isclaim:
        isclaim.clear()
        isclaim.append("off")
        return await event.edit("**- تم بنجاح ايقاف عملية الصيد**")
    elif "off" in isclaim:
        return await event.edit("**- لم يتم تفعيل الصيد بالأصل لأيقافه**")
    else:
        return await event.edit("**- لقد حدث خطأ ما وتوقف الامر لديك**")


@zq_lo.rep_cmd(pattern="ايقاف التثبيت")
async def _(event):
    if "on" in isauto:
        isauto.clear()
        isauto.append("off")
        return await event.edit("**- تم بنجاح ايقاف عملية التثبيت**")
    elif "off" in isauto:
        return await event.edit("**- لم يتم تفعيل التثبيت بالأصل لأيقافه**")
    else:
        return await event.edit("**-لقد حدث خطأ ما وتوقف الامر لديك**")


@zq_lo.rep_cmd(pattern="حالة الصيد")
async def _(event):
    if "on" in isclaim:
        await event.edit(f"**- الصيد وصل لـ({trys[0]}) **من المحاولات")
    elif "off" in isclaim:
        await event.edit("**- الصيد بالاصل لا يعمل .**")
    else:
        await event.edit("- لقد حدث خطأ ما وتوقف الامر لديك")


@zq_lo.rep_cmd(pattern="حالة التثبيت")
async def _(event):
    if "on" in isauto:
        await event.edit(f"**- التثبيت وصل لـ({trys2[0]}) من المحاولات**")
    elif "off" in isauto:
        await event.edit("**- التثبيت بالاصل لا يعمل .**")
    else:
        await event.edit("-لقد حدث خطأ ما وتوقف الامر لديك")
