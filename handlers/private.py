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

💠 /oynat - __Şarkıyı oynatır.__
💠 /dur - __Şarkıyı durdurur.__
💠 /basla - __Şarkıyı devam ettirir.__
💠 /gec - __Diğer şarkıya geçer.__
💠 /kapat - __Botu kapatır.__
💠 /sarkibul - __Şarkı aratır.__

Grubunuza özel müzik botu yaptırmak için @MoolRehber.

**🤖 Developer By @Zep_Unb**

        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sohbet Grubu 💬", url="https://t.me/ms_sohbet"
                    ),
                    InlineKeyboardButton(
                        "Müzik Kanalı 🎶", url="https://t.me/akarsumuzik"
                    )
                ]
            ]
        )
    )
