#    Copyright (C) 2024  Repthon Source
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    T.me/Repthon - T.me/E_7_V
try:
    from . import BASE, SESSION
except ImportError as e:
    raise Exception("Memes For Repthon") from e
from sqlalchemy import Column, Numeric, String, UnicodeText


class RepthonMemes(BASE):
    __tablename__ = "repthon_funs"
    meme_txt = Column(String(255), primary_key=True)
    meme_id = Column(String(255))

    def __init__(self, meme_txt, meme_id):
        self.meme_txt = str(meme_txt)
        self.meme_id = str(meme_id)

RepthonMemes.__table__.create(bind=SESSION.get_bind(), checkfirst=True)


def get_alll_memes():
    try:
        return SESSION.query(RepthonMemes).all()
    finally:
        SESSION.close()


def get_memes(meme_txt):
    memes = SESSION.query(RepthonMemes).get(str(meme_txt))
    if memes:
        return memes.meme_id
    else:
        return None


def add_memes(meme_txt, meme_id):
    memes = RepthonMemes(str(meme_txt), str(meme_id))
    SESSION.add(memes)
    SESSION.commit()


def remove_memes(meme_txt):
    memes = SESSION.query(RepthonMemes).get(str(meme_txt))
    if memes:
        SESSION.delete(memes)
        SESSION.commit()


def remove_all_memes():
    saved_memes = SESSION.query(RepthonMemes)
    if saved_memes:
        saved_memes.delete()
        SESSION.commit()
