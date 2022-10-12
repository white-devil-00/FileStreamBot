# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from multiprocessing.connection import Client
from ...vars import Var
from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.bot import StreamBot
from WebStreamer.utils.database import Ban_List
ban = Ban_List(Var.DATABASE_URL, Var.SESSION_NAME)


@StreamBot.on_message(filters.command(["start","Start"]))
async def start(b: Client, m: Message):
    if  await ban.is_user_exist(m.from_user.id):
        await m.reply(
            f'__Mr.{m.from_user.first_name},__'
                    )
        await m.reply(
            f'**Ｙｏｕ＇ｒｅ Ｂａｎｎｅｄ ．．．**'
                    )
    else:
        await m.reply(
            f'__Hi {m.from_user.mention(style="md")}, I\'m File to Link Bot__\n**__Send me a file to get an instant stream link ...__**'
        )

@StreamBot.on_message(filters.command(["help","Help"]))
async def help_menu(_, m: Message):
    if  await ban.is_user_exist(m.from_user.id):
        await m.reply(
            f'__Mr.{m.from_user.first_name},__'
                    )
        await m.reply(
            f'**Ｙｏｕ＇ｒｅ Ｂａｎｎｅｄ ．．．**'
                    )
    else:
        await m.reply_text(
            text="**┣⪼ ᴊᴜꜱᴛ ᴀ ꜱᴇɴᴅ ᴍᴇ ᴀ ꜰɪʟᴇ/ᴠɪᴅᴇᴏ, ɪ'ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴀ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ...\n\n┣⪼ ʏᴏᴜ ᴄᴀɴ ᴀʟꜱᴏ ᴜꜱᴇ ᴛʜᴇ ꜱᴀᴍᴇ ʟɪɴᴋ ꜰᴏʀ ꜱᴛʀᴇᴀᴍɪɴɢ\n\n┣⪼ ꜰᴏʀ ꜱᴜᴘᴘᴏʀᴛ : @F2LSupport\n\n┣⪼ ʙᴏᴛ ᴇᴛʜᴜᴍ ᴍᴀᴋᴋᴀʀ ᴘᴀɴɴᴜᴄʜᴜɴᴀ,\nᴀᴛʜᴜᴋᴜ ᴄᴏᴍᴘᴀɴʏ ᴘᴏʀᴜᴘᴀᴀɢᴀᴛʜᴜ 🙄**", 
            disable_web_page_preview=True
        )

@StreamBot.on_message(filters.command(["about","About"]))
async def help_menu(_, m: Message):
    if  await ban.is_user_exist(m.from_user.id):
        await m.reply(
            f'__Mr.{m.from_user.first_name},__'
                    )
        await m.reply(
            f'**Ｙｏｕ＇ｒｅ Ｂａｎｎｅｄ ．．．**'
                    )
    else:
        await m.reply_text(
            text="""<b>𝚂𝙾𝙼𝙴𝚃𝙷𝙸𝙽𝙶 𝙰𝙱𝙾𝚄𝚃 𝙼𝙴</b>

    <b>╭━━━━━━━〔𝙵𝙸𝙻𝙴-𝚃𝙾-𝙻𝙸𝙽𝙺 𝙱𝙾𝚃〕</b>
    ┃
    ┣⪼<b>𝙲𝚁𝙴𝙰𝚃𝙾𝚁-𝙽𝙰𝙼𝙴 : 𝚆𝙷𝙸𝚃𝙴 𝙳𝙴𝚅𝙸𝙻</b>
    ┣⪼<b>𝚂𝙴𝚁𝚅𝙴𝚁 : 𝙷𝙴𝚁𝚄𝙺𝙾</b>
    ┣⪼<b>𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 : 𝙿𝚈𝚃𝙷𝙾𝙽 3</b>
    ┣⪼<b>𝚂𝙾𝚄𝚁𝙲𝙴-𝙲𝙾𝙳𝙴 : <a href='https://NaKule.Setha.Payele'>𝙵𝙸𝙻𝙴-𝚃𝙾-𝙻𝙸𝙽𝙺</a></b>
    ┃
    <b>╰━━━━━━━〔𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝚄𝚂〕</b>""",
            disable_web_page_preview=True
        )

#Ban Feature Commands
@StreamBot.on_message(filters.command('add') & filters.private & filters.user(Var.OWNER_ID))
async def start(b, m):
    banid = m.reply_to_message.text
    if  await ban.is_user_exist(banid):
        await b.send_message(
                        chat_id=m.chat.id,
                        text="**__User is Already Banned !__**"
                    )
        return
    else:
        await ban.add_user(str(banid))
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#Ban\nUser id : {banid} is Banned by [{m.from_user.first_name}](tg://user?id={m.from_user.id})!"
        )
        await b.send_message(
                        chat_id=m.chat.id,
                        text=f"__Banned - {banid} !__"
                    )

@StreamBot.on_message(filters.command('clear') & filters.private & filters.user(Var.OWNER_ID) )
async def start(b, m):
    banid=m.reply_to_message.text
    if  await ban.is_user_exist(banid):
        await ban.delete_user(banid)
        await b.send_message(
                        chat_id=m.chat.id,
                        text=f"**__Unbanned - {banid} :)__**"
                    )
        await b.send_message(
                Var.BIN_CHANNEL,
                f"#Banned User id : {banid} unbanned by [{m.from_user.first_name}](tg://user?id={m.from_user.id})!"
            )
        return
    else:
        await b.send_message(
                        chat_id=m.chat.id,
                        text=f"**__User is Not Banned__** 😶"
                    )

@StreamBot.on_message(filters.command('ban_list') & filters.private )
async def BanList(b,m):
    total_users = await ban.total_users_count()
    await m.reply_text(text=f"**Total No.Of Users Banned : ** `{total_users}`")
    return