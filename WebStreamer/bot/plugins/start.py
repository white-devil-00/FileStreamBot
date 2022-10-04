# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.bot import StreamBot


@StreamBot.on_message(filters.command(["start", "help"]))
async def start(_, m: Message):
    await m.reply(
        f'__Hi {m.from_user.mention(style="md")},__ **__I\'m File to Link Bot__**\nz**Send me a file to get an instant stream link.**"'
    )
