import sys
import time

from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.errors import AccessTokenExpiredError, AccessTokenInvalidError
from ..Config import Config
from .bothseesion import bothseesion
from .client import RepUserBotClient
from .logger import logging

LOGS = logging.getLogger("ريبـــثون")
__version__ = "3.10.3"

loop = None

if Config.STRING_SESSION:
    session = bothseesion(Config.STRING_SESSION, LOGS)
else:
    session = "baqir"

try:
    zq_lo = RepUserBotClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(
        f"STRING_SESSION CODE WRONG MAKE A NEW SESSION - {e}\n كود سيشن تيليثـون غير صالح .. قم باستخـراج كود جديد ؟!"
    )
    sys.exit()


try:
    zq_lo.tgbot = tgbot = RepUserBotClient(
        session="RepTgbot",
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    ).start(bot_token=Config.APP_TOKEN)
except FloodWaitError as e:
    LOGS.error(f"FloodWaitError: فلود وايت - يرجى الانتظار لـ {e.seconds} ثانية.")
    time.sleep(e.seconds)
except (AccessTokenExpiredError, AccessTokenInvalidError):
    LOGS.error("توكن البوت غير صالح قم باستبداله بتوكن جديد من بوت فاذر")
