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
    log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
    stream_link = f"{Var.URL}{log_msg.id}/{quote_plus(get_name(m))}?hash={get_hash(log_msg)}"
    short_link = f"{Var.URL}{get_hash(log_msg)}{log_msg.id}"
    logging.info(f"Generated link: {stream_link} for {m.from_user.first_name}")
    rm = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Open", url=stream_link)]]
    )
    def get_media_file_size(m):
        media = m.video or m.audio or m.document
        if media and media.file_size:
            return media.file_size
        else:
            return None

    if Var.FQDN == Var.BIND_ADDRESS:
        # dkabl
        rm = None
    await m.reply_text(
        text="FileName 📂: {}\nFileSize 💾:{}\nDowload Link 📥: {}\n{}".format(
            get_name(m), get_media_file_size(m), short_link, get_size(m)
        ),
        quote=True,
        parse_mode=ParseMode.HTML,
        reply_markup=rm,
    )
    await log_msg.reply_text(text=f"Requested by [{m.from_user.first_name}](tg://user?id={m.from_user.id})\nUser ID :- `{m.from_user.id}`\nDownload Link :- {shot_link}")
