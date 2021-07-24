from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Selam Ben {bn}**

`Sesli sohbetlerde güvenli bir şekilde müzik dinlemenize olanak sağlarım.`

          **📜 Kullanım Kılavuzu 📜**

💠 /play - __Şarkıyı oynatır.__
💠 /pause - __Şarkıyı durdurur.__
💠 /resume - __Şarkıyı devam ettirir.__
💠 /skip - __Diğer şarkıya geçer.__
💠 /stop - __Botu kapatır.__
💠 /song - __Şarkı aratır.__

**🤖 Dev By @Zep_Unb**

        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Özel Müzik Botu Yaptırmak İçin", url="https://t.me/MoolRehber/7"
                    ),
                    InlineKeyboardButton(
                        "Destek Grubu 🛡", url="https://t.me/DepressionalistChat"
                    )
                ]
            ]
        )
    )
