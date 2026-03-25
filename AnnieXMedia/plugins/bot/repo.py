# Authored By Certified Coders © 2025
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnnieXMedia import app
from config import BOT_USERNAME

repo_caption = """**
ʜᴇʏ ʙᴀʙʏ 👋
ᴛʜᴇ ᴄᴏᴅᴇ ғᴏʀ ᴛʜɪs ʙᴏᴛ ɪs ᴘʀɪᴠᴀᴛᴇ 🔒
ɪᴛ’s ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ᴛᴏ sʜᴀʀᴇ ʀɪɢʜᴛ ɴᴏᴡ ✨
ᴘʟᴇᴀsᴇ ᴅᴏɴ’ᴛ ᴀsᴋ ғᴏʀ ᴛʜᴇ ʀᴇᴘᴏ 🙌
ᴛʜᴀɴᴋs ғᴏʀ ᴜɴᴅᴇʀsᴛᴀɴᴅɪɴɢ 🤍
**"""

@app.on_message(filters.command("repo"))
async def show_repo(_, msg):
    buttons = [
        [InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✨", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [
            InlineKeyboardButton("👑 ᴏᴡɴᴇʀ", url="https://t.me/II_YOUR_MADARA_II"),
            InlineKeyboardButton("💬 ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/MADARA_DEFAULTER_ABOUT")
        ],
        [
            InlineKeyboardButton("🛠️ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/FRIEND_ZONE_BY_MADARA")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    try:  
        await msg.reply_photo(
            photo="https://files.catbox.moe/tvjyn9.jpg",
            caption=repo_caption,
            reply_markup=reply_markup
        )
    except:
        pass
