import threading

from sqlalchemy import Column, String

from . import BASE, SESSION


class TedeChatapp(BASE):
    __tablename__ = "tede_chatapp"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = str(chat_id)


TedeChatapp.__table__.create(bind=SESSION.get_bind(), checkfirst=True)

INSERTION_LOCK = threading.RLock()


def is_tede(chat_id):
    try:
        chat = SESSION.query(TedeChatapp).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_tede(chat_id):
    with INSERTION_LOCK:
        tedechat = SESSION.query(TedeChatapp).get(str(chat_id))
        if not tedechat:
            tedechat = TedeChatBot(str(chat_id))
        SESSION.add(tedechat)
        SESSION.commit()


def rem_tede(chat_id):
    with INSERTION_LOCK:
        tedechat = SESSION.query(TedeChatapp).get(str(chat_id))
        if tedechat:
            SESSION.delete(tedechat)
        SESSION.commit()
