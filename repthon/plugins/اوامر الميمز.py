import random
from telethon import events
import random, re

from repthon.utils import admin_cmd

import asyncio
from repthon import zq_lo

from ..core.managers import edit_or_reply


plugin_category = "الترفيه"



@zq_lo.on(admin_cmd(outgoing=True, pattern="بصمات ميمز$"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        " قائمة بصمات الميمز\n★⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n⎉╎اختر احدى هذه الاوامر\n\n- ( `.تخوني` )\n- ( `.مستمرة الكلاوات` )\n- ( `.احب العراق` )\n- ( `.احبك` )\n- ( `.اخت التنيج` )\n- ( `.اذا اكمشك` )\n- ( `.اسكت` )\n- ( `.افتهمنا` )\n- ( `.اكل خرا` )\n- ( `.العراق` )\n- ( `.الكعده وياكم` )\n\n★⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n⎉╎CH : @Repthon"

)

@zq_lo.on(admin_cmd(outgoing=True, pattern="بصمات ميمز2$"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        " قائمة بصمات الميمز\n★⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n⎉╎ اختر احدى هذه الاوامر\n\n- ( `.الكمر اني` )\n- ( `.اللهم لا شماته` )\n- ( `.اني مااكدر` )\n- ( `.بقولك ايه` )\n- ( `.تف على شرفك` )\n- ( `.شجلبت` )\n- ( `.شكد شفت ناس` )\n- ( `.صباح القنادر` )\n- ( `.ضحكة فيطية` )\n- ( `.طاهر القلب` )\n- ( `.غطيلي` )\n\n★⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n⎉╎CH : @Repthon"

)

@zq_lo.on(admin_cmd(outgoing=True, pattern="بصمات ميمز3$"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        " قائمة اوامر بصمات الميمز\n★⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n⎉╎ اختر احدى هذه الاوامر\n\n- ( `.في منتصف الجبهة` )\n- ( `.لاتقتل المتعه` )\n- ( `.لا لتغلط` )\n- ( `.لا يمه لا` )\n- ( `.لحد يحجي وياي` )\n- ( `.ماادري يعني` )\n- ( `.منو انت` )\n- ( `.مو صوجكم` )\n- ( `.خوش تسولف` )\n- ( `.يع` )\n- ( `.زيج` )\n- ( `.زيج2` )\n\n★⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n⎉╎CH : @Repthon"

)

@zq_lo.on(admin_cmd(outgoing=True, pattern="بصمات ميمز4$"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        " قائمة اوامر بصمات الميمز\n★⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n⎉╎ اختر احدى هذه الاوامر\n\n- ( `.يعني مااعرف` )\n- ( `.يامرحبا` )\n- ( `.منو انتة` )\n- ( `.ماتستحي` )\n- ( `.كعدت الديوث` )\n- ( `.عيب` )\n- ( `.عنعانم` )\n- ( `.طبك مرض` )\n- ( `.سييي` )\n- ( `.سبيدر مان` )\n- ( `.خاف حرام` )\n- ( `.تحيه لاختك` )\n\n★⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n⎉╎CH : @Repthon"

)
	
@zq_lo.on(admin_cmd(outgoing=True, pattern="بصمات ميمز5$"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        " قائمة اوامر بصمات الميمز\n★⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n⎉╎ اختر احدى هذه الاوامر\n\n- ( `.امشي كحبة` )\n- ( `.امداك` )\n- ( `.الحس` )\n- ( `.افتهمنا` )\n- ( `.اطلع برا` )\n- ( `.اخت التنيج` )\n- ( `.اوني تشان` )\n- ( `.اوني تشان2` )\n- ( `.بجيت` )\n- ( `.نشاقة` )\n- ( `.لاتغلط` )\n- ( `.احب الله` )\n- ( `.روح` )\n- ( `.خبز يابس` )\n- ( `.خيار بصل` )\n- ( `.ماي ارو` )\n- ( `.ولك حشاش` )\n- ( `.انت شرايود` )\n- ( `.بالعباس` )\n\n\n⎉╎CH : @Repthon"

)
@zq_lo.on(admin_cmd(outgoing=True, pattern="بصمات انمي$"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
       " قائمة اوامر بصمات الانمي\n★⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n⎉╎ اختر احدى هذه الاوامر\n\n- ( `.انمي1` )\n- ( `.انمي2` )\n- ( `.انمي3` )\n- ( `.انمي4` )\n- ( `.انمي5` )\n- ( `.انمي6` )\n- ( `.انمي7` )\n- ( `.انمي8` )\n- ( `.انمي9` )\n- ( `.انمي10` )\n\n★⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n⎉╎CH : @Repthon"
	
)
