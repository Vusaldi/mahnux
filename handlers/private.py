from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://images.app.goo.gl/in11Pj1tHNhVo4DY9",
                caption=(f"""**Salam {message.from_user.mention} 🎧\nMən {bot}!\nSəsli Söhbətlərdə Musiqi Oxuyan Botam. Ban Yetgisi Olmadan, Səs Yetkisi Verib, Asistanı Qrupa Əlavə Edin.\n\nSahibim 👉  [KPLGƏ](https://t.me/sesizKOLGE)**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕  Məni Qrupa Əlavə Et ➕", url=f"https://t.me/kolgempbot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 ASİSTAN", url="https://t.me/KolgeMp3Asistan"
                    ),
                    InlineKeyboardButton(
                        "⚡ DİGƏR BOTLARIM", url="https://t.me/menimbotlarim"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 ƏMİRLƏR" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "🇦🇿 OWNER 👨‍💻 ", url=f"https://t.me/sesizKOLGE"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text("    ❗ Qeyd:\n Botun Aktiv İşləməsi Üçün Bu Üç Yetkiyə Ehdiyacı Var:\n- Mesaj Silmə Yetkisi,\n- Bağlantı İlə Dəvət Etmə Yetkisi,\n- Səsli SÖhbəti Yönətmə Uetkisi.", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "💂‍♂️ İstifatəçi Əmrləri", callback_data="herkes")
                 ],[                     
                     InlineKeyboardButton(
                         "🕵️‍♂️ Admin  Əmrləri", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "Geri 🔄", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "🇦🇿 OWNER 👨‍💻", url="https://t.me/sesizKOLGE")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text("    ❗ Qeyd:\nBotun Aktiv İşləməsi Üçün Bu Üç Yetkiyə Ehdiyacı Var\n- Mesaj Silmə Yetkisi.\n- Bağlantı İlə Dəvət Etmə Yetkisi.\n- Səsli Söhbəti Yönətmə Yetkisi.", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "💂‍♂️👮‍♂️ Hərkəs üçün əmrlər", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "👮‍♂️ Admin əmrləri",callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "🔄 Geri", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "🇦🇿 OWNER 👨‍💻", url="https://t.me/sesizKOLGE")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>👋 Salam {query.from_user.mention}!\n🕵️‍♂️ 💂‍♂️ Bu Botun Hərkəs Üçün Əmr Menyusudu\n\n ▶️ /play - Musiqi Adı Sənıtci Adı\n ▶️ /play - Musiqi YouTube Lingi\n 🎧 /song - Sürətli Şəkildə Musiqi Yükləyin\n🎬 /vsong - Sürətli Şəkildə Vidyo Yükləyin\n 🔍 /search - Oxşar Musiqi Və Vidyoları Axtar\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🇦🇿 OWNER 👨‍💻", url="https://t.me/sesizKOLGE")
                 ],
                 [
                     InlineKeyboardButton(
                         "️🔄 Geri", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>👋 Salam {query.from_user.mention}!\n🕵️‍♂️ Bu Botun Adminlər Üçün Əmr menyusudu\n\n ⏸ /resume - Musiqi Oxutmağa Davam Et\n ⏸▶️ /pause - Musiqini Dayandır\n ⏩ /skip - Sıraya alınmış musiqiyə keç\n ⏹ /skip - Növbəyə Alınmış Musiqiyə Keçər\n 🔼 /yetkiver - Userə Səsli Söhbətdə İdarəÇilik Yetkisi Verər \n 🔽 /yetkial - Userin Səsli Söhbət İdarəçi Yeykisin Alar\n\n ⚪ /asistan - Musiqi Asistanı Qrupunuza Qoşar\♻️ /reload - Botu Yenidən Başladar\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "Sahib 🇦🇿", url="https://t.me/sesizKOLGE")
                 ],
                 [
                     InlineKeyboardButton(
                         "️🔄 Geri", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**Salam {query.from_user.mention} 🎵\nMən {bot}!\nSəsli sohbətlərdə musiqi oxuyan botam. Ban yetkisiz, Səs yönətim yetki verib, Asistanı qrupa əlavə edin.\n\nSahibim👉  [Ulvi](https://t.me/BrendUIvi)**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Məni Qrupa Əlavə Et ❱ ➕", url=f"https://t.me/Kolgempbot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 ASİSTAN", url="https://t.me/KolgeMp3Asistan"
                    ),
                    InlineKeyboardButton(
                        "⚡ DİGƏR BOTLARIM", url="https://t.me/MorphinChat"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 ƏMİRLƏR" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "🇦🇿 OWNER 👨‍💻", url=f"https://t.me/sesizKOLGE"
                    )
                ]
                
           ]
        ),
    )
