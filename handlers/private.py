from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Selam Ben {bn}**

`Sesli sohbetlerde müzik dinlemenize olanak sağlarım.`

          **📜 Kullanım Kılavuzu 📜**

💠 /play - __Şarkıyı oynatır.__
💠 /pause - __Şarkıyı durdurur.__
💠 /resume - __Şarkıyı devam ettirir.__
💠 /skip - __Diğer şarkıya geçer.__
💠 /stop - __Botu kapatır.__
💠 /song - __Şarkı aratır.__

__Grubunuza özel müzik botu yaptırmak için @MoolRehber__

**🤖 Developer By @Zep_Unb**

        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Bot Yaptırmak İçin 🤖", url="https://t.me/Zep_Unb"
                    ),
                    InlineKeyboardButton(
                        "Destek Kanalı 🔰", url="https://t.me/MoolRehber"
                    )
                ]
            ]
        )
    )
