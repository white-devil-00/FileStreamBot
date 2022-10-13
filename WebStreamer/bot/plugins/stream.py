# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

import logging
from WebStreamer.utils.file_properties import get_size
from pyrogram import filters
from WebStreamer.vars import Var
from urllib.parse import quote_plus
from WebStreamer.bot import StreamBot
from WebStreamer.utils import get_hash, get_name
from WebStreamer.utils.human_readable import humanbytes
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from WebStreamer.utils.database import Ban_List
ban = Ban_List(Var.DATABASE_URL, Var.SESSION_NAME)





@StreamBot.on_message(
    filters.private
    & (
        filters.document
        | filters.video
        | filters.audio
        | filters.animation
        | filters.voice
        | filters.video_note
        | filters.photo
        | filters.sticker
    ),
    group=4,
)
async def media_receive_handler(_, m: Message):
    if  await ban.is_user_exist(m.from_user.id):
        if m.from_user.last_name == None:
            name=m.from_user.first_name
        else:
             name=m.from_user.first_name+" "+m.from_user.last_name
        await m.reply(
            f'__Sorry Mr.{name},__'
                    )
        await m.reply(
            f'**Ｙｏｕ＇ｒｅ Ｂａｎｎｅｄ ．．．**'
                    )
    else:
        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = f"{Var.URL}{log_msg.id}/{quote_plus(get_name(m))}?hash={get_hash(log_msg)}"
        short_link = f"{Var.URL}{get_hash(log_msg)}{log_msg.id}"
        logging.info(f"Generated link: {stream_link} for {m.from_user.first_name}")
        rm = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Ｄｏｗｎｌｏａｄ 🔗", url=stream_link)]]
        )


        if Var.FQDN == Var.BIND_ADDRESS:
            # dkabl
            rm = None
        await m.reply_text(
            text="""
<b>📧 ғɪʟᴇ ɴᴀᴍᴇ :- </b> <i><b>{}</b></i>

<b>📦 ғɪʟᴇ sɪᴢᴇ :- </b> <i><b>{}</b></i>

<b>💌 ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ :- </b> <i><b>{}</b></i>""".format(
                get_name(m), humanbytes(get_size(m)), short_link
            ),
            quote=True,
            parse_mode=ParseMode.HTML,
            reply_markup=rm,
        )
        await log_msg.reply_text(text=f'<b>Requested by {m.from_user.mention(style="md")}\nUser ID :- `{m.from_user.id}`\nDownload Link :- {short_link}</b>')
