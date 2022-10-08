# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

import logging
import asyncio
from pyrogram import filters, Client
from WebStreamer.vars import Var
from urllib.parse import quote_plus
from WebStreamer.bot import StreamBot
from WebStreamer.utils import get_hash, get_name, get_size
from WebStreamer.utils.human_readable import humanbytes
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait, UserNotParticipant


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
async def private_receive_handler(c: Client, m: Message):
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await c.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "banned" | user == "banned":
                await c.send_message(
                    chat_id=m.chat.id,
                    text=f"**𝚈𝙾𝚄 𝙰𝚁𝙴 𝙱𝙰𝙽𝙽𝙴𝙳../**"
                )
                return
        except UserNotParticipant:
            await c.send_message(
                chat_id=m.chat.id,
                    text="**𝙹𝙾𝙸𝙽 𝚃𝙷𝙴 𝚄𝙿𝙳𝙰𝚃𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃..**\n**𝙱𝙴𝙲𝙰𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙸𝚂 𝙰 𝚃𝙴𝚂𝚃 𝙱𝙾𝚃!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("𝙹𝙾𝙸𝙽 𝚄𝙿𝙳𝙰𝚃𝙴𝚉 𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                )
            )
            return
        except Exception:
            await c.send_message(
                chat_id=m.chat.id,
                text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                parse_mode="Markdown",
                disable_web_page_preview=True)
            return
    try:
        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = f"{Var.URL}{log_msg.id}/{quote_plus(get_name(m))}?hash={get_hash(log_msg)}"
        short_link = f"{Var.URL}{get_hash(log_msg)}{log_msg.id}"
        logging.info(f"Generated link: {stream_link} for {m.from_user.first_name}")
        filesize=humanbytes(get_size(m))
        rm = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Ｄｏｗｎｌｏａｄ 🔗", url=stream_link)]]
        )


        if Var.FQDN == Var.BIND_ADDRESS:
            # dkabl
            rm = None
        await m.reply_text(
            text="<b>📂 𝙵𝚒𝚕𝚎𝙽𝚊𝚖𝚎 : \n{}\n💾 𝙵𝚒𝚕𝚎𝚂𝚒𝚣𝚎 : {}\n📥 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍 𝙻𝚒𝚗𝚔 : {}</b>".format(
                get_name(m), filesize, short_link
            ),
            quote=True,
            parse_mode=ParseMode.HTML,
            reply_markup=rm,
        )
        await log_msg.reply_text(text=f"**Requested by [{m.from_user.first_name}](tg://user?id={m.from_user.id})\nUser ID :- `{m.from_user.id}`\nDownload Link :- {short_link}***")
    except FloodWait as e:
        print(f"Sleeping for {str(e.x)}s")
        await asyncio.sleep(e.x)
        await c.send_message(chat_id=Var.BIN_CHANNEL, text=f"Gᴏᴛ FʟᴏᴏᴅWᴀɪᴛ ᴏғ {str(e.x)}s from [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**𝚄𝚜𝚎𝚛 𝙸𝙳 :** `{str(m.from_user.id)}`", disable_web_page_preview=True, parse_mode="Markdown")