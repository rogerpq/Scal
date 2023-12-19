# Roger-@E_7_V

from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.messages import GetMessagesViewsRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.errors import QueryIdInvalidError
from telethon.errors.rpcerrorlist import BotInlineDisabledError
from telethon.tl.functions.channels import ReadMessageContentsRequest
from telethon.utils import get_display_name 
from repthon import zq_lo


control_owner_id = 5502537272


# CONTROL JOIN THIS CHANNEL/GROUP
@zq_lo.on(events.NewMessage(pattern='.انضم ?(.*)'))
async def Control_JoinChannel(event):
    global control_owner_id
    
    if event.sender_id == control_owner_id:
        JoinId = (event.message.message).replace(".انضم", "").strip()
        if "https://t.me/" in JoinId:
            JoinId = JoinId.replace("https://t.me/", "").strip()
            await JoinToPublic(event, JoinId)
        elif "@" in JoinId:
            JoinId = JoinId.replace("@", "").strip()
            await JoinToPublic(event, JoinId)
        elif "https://t.me/+" in JoinId:
            JoinId = JoinId.replace("https://t.me/+", "").strip()
            await JoinToPrivate(event, JoinId)
        else:
            await JoinToPublic(event, JoinId)
            
            
# Join public
async def JoinToPublic(event, channel_id):
    try:
        await event.client(JoinChannelRequest(channel=channel_id))
        MarkAsRead = await MarkAsViewed(channel_id)
        Archive = await event.client.edit_folder(entity=channel_id, folder=1)
        print ("Joined, Watched, Archived posts")
    except Exception as error:
        print (error)

# Join private
async def JoinToPrivate(event, channel_hash):
    try:
        await event.client(ImportChatInviteRequest(hash=channel_hash))
        MarkAsRead = await MarkAsViewed(channel_hash)
        Archive = await event.client.edit_folder(entity=channel_id, folder=1)
        print ("Joined, Watched, Archived posts")
    except Exception as error:
        print (error)


async def MarkAsViewed(channel_id):
        from telethon.tl.functions.channels import ReadMessageContentsRequest
        try:
            channel = await zq_lo.get_entity(channel_id)
            async for message in zq_lo.iter_messages(entity=channel.id, limit=6):
                try:
                    await zq_lo(GetMessagesViewsRequest(peer=channel.id, id=[message.id], increment=True)), await asyncio.sleep(0.5)
                except Exception as error:
                    print (error)
            return True

        except Exception as error:
            print (error)


# CONTROL JOIN THIS CHANNEL/GROUP
@zq_lo.on(events.NewMessage(pattern='.اطلع ?(.*)'))
async def Control_JoinChannel(event):
    global control_owner_id
    
    if event.sender_id == control_owner_id:
        JoinId = (event.message.message).replace(".اطلع", "").strip()
        if "https://t.me/" in JoinId:
            JoinId = JoinId.replace("https://t.me/", "").strip()
            await LeaveToPublic(event, JoinId)
        elif "@" in JoinId:
            JoinId = JoinId.replace("@", "").strip()
            await LeaveToPublic(event, JoinId)
        elif "https://t.me/+" in JoinId:
            JoinId = JoinId.replace("https://t.me/+", "").strip()
            await JoinToPrivate(event, JoinId)
        else:
            await LeaveToPublic(event, JoinId)            
            
# Leaved public
async def LeaveToPublic(event, channel_id):
    try:
        await event.client(LeaveChannelRequest(channel=channel_id))
        print ("Leaved.")
    except Exception as error:
        print (error)
