# اصلاح نـمـى🔥

from datetime import datetime
from repthon import zq_lo
from ..core.managers import edit_delete, edit_or_reply

@zq_lo.rep_cmd(pattern="حساب العمر(?:\\s|$)([\\s\\S]*)")
async def _(event):
    yar_str = event.text[12:]
    if not yar_str:
        return await edit_or_reply(event, "**✾╎استخـدم الامـر كالتالـي .. حساب العمر + السنـة**")
    
    # Convert input year to integer
    try:
        yar = int(yar_str)
    except ValueError:
        return await edit_or_reply(event, "**✾╎يرجى إدخال عدد صحيح للسنة**")
    
    YearNow = datetime.now().year
    MyAge = YearNow - yar
    await edit_or_reply(event, "**🚹╎عمرك هـو :**  {}".format(MyAge))
