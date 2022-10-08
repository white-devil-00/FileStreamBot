# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from pyrogram.types import User, Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait, UserNotParticipant


@StreamBot.on_message(filters.command(["start","Start"]))
async def start(c, m: Message):
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await c.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "BANNED":
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

    await m.reply(
        f'__Hi {m.from_user.mention(style="md")}, I\'m File to Link Bot__\n**__Send me a file to get an instant stream link ...__**'
    )

@StreamBot.on_message(filters.command(["help","Help"]))
async def help_menu(_, m: Message):
    await m.reply(
        f"**┣⪼ 𝚂𝙴𝙽𝙳 𝙼𝙴 𝙰𝙽𝚈 𝙵𝙸𝙻𝙴/𝚅𝙸𝙳𝙴𝙾 𝚃𝙷𝙴𝙽 𝙸 𝚆𝙸𝙻𝙻 𝙶𝙸𝚅𝙴 𝚈𝙾𝚄 𝙿𝙴𝚁𝙼𝙰𝙽𝙴𝙽𝚃 𝚂𝙷𝙰𝚁𝙰𝙱𝙻𝙴 𝙻𝙸𝙽𝙺 𝙾𝙵 𝙸𝚃...\n\n┣⪼ 𝚃𝙷𝙸𝚂 𝙻𝙸𝙽𝙺 𝙲𝙰𝙽 𝙱𝙴 𝚄𝚂𝙴𝙳 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙾𝚁 𝚃𝙾 𝚂𝚃𝚁𝙴𝙰𝙼 𝚄𝚂𝙸𝙽𝙶 𝙴𝚇𝚃𝙴𝚁𝙽𝙰𝙻 𝚅𝙸𝙳𝙴𝙾 𝙿𝙻𝙰𝚈𝙴𝚁𝚂 𝚃𝙷𝚁𝙾𝚄𝙶𝙷 𝙼𝚈 𝚂𝙴𝚁𝚅𝙴𝚁.\n\n┣⪼ 𝙵𝙾𝚁 𝚂𝚃𝚁𝙴𝙰𝙼𝙸𝙽𝙶 𝙹𝚄𝚂𝚃 𝙲𝙾𝙿𝚈 𝚃𝙷𝙴 𝙻𝙸𝙽𝙺 𝙰𝙽𝙳 𝙿𝙰𝚂𝚃𝙴 𝙸𝚃 𝙸𝙽 𝚈𝙾𝚄𝚁 𝚅𝙸𝙳𝙴𝙾 𝙿𝙻𝙰𝚈𝙴𝚁 𝚃𝙾 𝚂𝚃𝙰𝚁𝚃 𝚂𝚃𝚁𝙴𝙰𝙼𝙸𝙽𝙶.\n\n┣⪼ 𝙵𝙾𝚁 𝙼𝙾𝚁𝙴 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 :- /about\n**" 
    )

@StreamBot.on_message(filters.command(["about","About"]))
async def about_menu(_, m: Message):
    await m.reply(
        f"""<b>𝚂𝙾𝙼𝙴𝚃𝙷𝙸𝙽𝙶 𝙰𝙱𝙾𝚄𝚃 𝙼𝙴</b>

<b>╭━━━━━━━〔𝙵𝙸𝙻𝙴-𝚃𝙾-𝙻𝙸𝙽𝙺 𝙱𝙾𝚃〕</b>
┃
┣⪼<b>𝙲𝚁𝙴𝙰𝚃𝙾𝚁-𝙽𝙰𝙼𝙴 : 𝚆𝙷𝙸𝚃𝙴 𝙳𝙴𝚅𝙸𝙻</b>
┣⪼<b>𝙱𝙾𝚃-𝚂𝙴𝚁𝚅𝙴𝚁 : 𝙷𝙴𝚁𝚄𝙺𝙾</b>
┣⪼<b>𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 : 𝙿𝚈𝚃𝙷𝙾𝙽</b>
┣⪼<b>𝚂𝙾𝚄𝚁𝙲𝙴-𝙲𝙾𝙳𝙴 : <a href='https://NaKule.Setha.Payele'>𝙵𝙸𝙻𝙴-𝚃𝙾-𝙻𝙸𝙽𝙺</a></b>
┃
<b>╰━━━━━━━〔𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝚄𝚂〕</b>"""
    )