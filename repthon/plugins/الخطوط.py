# Repthon - Roger
# © Repthon Team 2023
# ها شعدك داخل ع الملف تريد تخمط ؟ ابو زربة لهل درجة فاشل  

from telethon import events
from repthon import zq_lo
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..core.managers import edit_delete, edit_or_reply
from telethon import functions
from telethon.errors.rpcerrorlist import MessageIdInvalidError
from repthon.utils import admin_cmd


@zq_lo.on(admin_cmd(pattern="(خط الغامق|خط غامق)"))
async def btext(event):
    isbold = gvarstatus("bold")
    if not isbold:
        addgvar ("bold", "on")
        await edit_delete(event, "**⎉╎ تم تفعيل خط الغامق بنجاح ✓**")
        return

    if isbold:
        delgvar("bold")
        await edit_delete(event, "**⎉╎ تم اطفاء خط الغامق بنجاح ✓ **")
        return


@zq_lo.on(admin_cmd(pattern="(خط رمز|خط الرمز)"))
async def btext(event):
    isramz = gvarstatus("ramz")
    if not isramz:
        addgvar ("ramz", "on")
        await edit_delete(event, "**⎉╎ تم تفعيل خط الرمز بنجاح ✓**")
        return

    if isramz:
        delgvar("ramz")
        await edit_delete(event, "**⎉╎ تم اطفاء خط الرمز بنجاح ✓ **")
        return


@zq_lo.on(admin_cmd(pattern="(خط المشطوب|خط مشطوب)"))
async def btext(event):
    istshwesh = gvarstatus("tshwesh")
    if not istshwesh:
        addgvar ("tshwesh", "on")
        await edit_delete(event, "**⎉╎ تم تفعيل خط المشطوب بنجاح ✓**")
        return

    if istshwesh:
        delgvar("tshwesh")
        await edit_delete(event, "**⎉╎ تم اطفاء خط المشطوب بنجاح ✓**")
        return


@zq_lo.on(admin_cmd(pattern="(خط مائل|الخط المائل)"))  
async def btext(event):
    isitalic = gvarstatus("italic")
    if not isitalic:
        addgvar ("italic", "on")
        await edit_delete(event, "**⎉╎ تم تفعيل خط مائل بنجاح ✓**")
        return      
  
    if isitalic:
        delgvar("italic")
        await edit_delete(event, "**⎉╎ تم إطفاء خط مائل بنجاح ✓**")
        return


@zq_lo.on(events.NewMessage(outgoing=True))
async def baqir(event):
    isbold = gvarstatus("bold")
    if isbold and "." not in event.message.message:
        try:
            await event.edit(f"**{event.message.message}**")
        except MessageIdInvalidError:
            pass
            
    isramz = gvarstatus("ramz")
    if isramz and "." not in event.message.message:
        try:
            await event.edit(f"`{event.message.message}`")
        except MessageIdInvalidError:
            pass
            
    istshwesh = gvarstatus("tshwesh")
    if istshwesh and "." not in event.message.message:
        try:
            await event.edit(f"~~{event.message.message}~~")
        except MessageIdInvalidError:
            pass
            
    isitalic = gvarstatus("italic")
    if isitalic and "." not in event.message.message:
        try:
            await event.edit(f"__{event.message.message}__")
        except MessageIdInvalidError:
            pass
