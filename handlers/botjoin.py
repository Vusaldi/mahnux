from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["qosul", "asistan"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>ℹ Məni Əvvəlcə Admim Etməlisiniz</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "Sesmusic Asistan"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"Sənin İsdədiyin Üçün Gəldim")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>⚡Asistan Onsuzda Bu Qrupda Var</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🔵 Zaman Aşımı Hatası 🔵\n User {user.first_name} userbot için yoğun katılma istekleri nedeniyle grubunuza katılamadı! Asistanın grupta yasaklanmadığından emin olun."
            "\n\n Yada Asistan Hesabını Qrupa özün əlavə et </b>",
        )
        return
    await message.reply_text(
            "<b>⚡ Asistan Onsuzda Bu Qrupda Var</b>",
        )
    
@USER.on_message(filters.group & filters.command(["ayrıl", "asistanby"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>⚡ Asistan Qrupunuzdan Ayrılamadı!."
            "\n\n✔ Yada Özün Çıxara Bilərsən</b>",
        )
        return
 
 
 
