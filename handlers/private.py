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

🤖 @Zep_Unb tarafından @bidelio'ya özel kodlanmıştır.
**Siz de özel bot yaptırmak istiyorsanız @Zep_Unb ile iletişime geçebilirsiniz.**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Destek Grubu", url="https://t.me/MoolRehber"
                    ),
                    InlineKeyboardButton(
                        "Özel Bot Yaptırmak İçin", url="https://t.me/MoolRehber/7"
                    )
                ]
            ]
        )
    )
