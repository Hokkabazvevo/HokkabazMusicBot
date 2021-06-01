from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""Selam Ben {bn}

__Sesli sohbetlerde müzik dinlemenize olanak sağlarım.__

          📜Kullanma Kılavuzu📜

💠 /play - Şarkıyı oynatır.
💠 /pause - Şarkıyı durdurur.
💠 /resume - Şarkıyı devam ettirir.
💠 /skip - Diğer şarkıya geçer.
💠 /stop - Botu kapatır.
💠 /song - Şarkı aratır.

🤖 Developer By @Zep_Unb

**Grubunuza özel müzik botu yaptırmak için sahibim ile iletişime geçebilirsiniz.**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sohbet Grubumuz", url="https://t.me/DepressionalistChat"
                    ),
                    InlineKeyboardButton(
                        "Grubunuza Özel Bot Yaptırmak İçin", url="https://t.me/MoolRehber"
                    )
                ]
            ]
        )
    )
