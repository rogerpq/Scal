#Repthon

from datetime import datetime

from repthon import zq_lo
from ..core.managers import edit_delete, edit_or_reply


@zq_lo.rep_cmd(pattern="حساب العمر(?:\\s|$)([\\s\\S]*)")
async def _(event):
    yar = event.text[12:]
    if not yar:
       return await edit_or_reply(event, "**✾╎استخـدم الامـر كالتالـي .. حساب العمر + السنـه**")
    YearNow = datetime.now().year
    MyAge = YearNow - yar
    await edit_or_reply(e, "**🚹╎عمرك هـو :**  {}".format(MyAge))
