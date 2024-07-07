from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PAKHIMUSIC import app
from config import BOT_USERNAME

start_txt = """**
✪ 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐏𝐀𝐊𝐇𝐈 𝐌𝐔𝐒𝐈𝐂 𝐑𝐄𝐏𝐎 ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
     
            [ 
            InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
     
            [
             InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/Emergency_Gamer"),
             InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/Emergency_Gamer"),
             ],
     
             [
             InlineKeyboardButton("𝗟𝗜𝗩𝗘 𝗖𝗖", url="https://t.me/Emergency_Gamer"),
             ],
     
             [
             InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚𝗕𝗢𝗧", url=f"https://t.me/Emergency_Gamer"),            
             InlineKeyboardButton("︎𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/Emergency_Gamer"),
             ],
     
             [
             InlineKeyboardButton("𝐄𝐕𝐈𝐋", url=f"https://t.me/Emergency_Gamer"),
             InlineKeyboardButton("𝐁𝐀𝐍 𝐀𝐋𝐋", url=f"https://t.me/Emergency_Gamer"),
             ],
     
             [
             InlineKeyboardButton("𝐀𝐋𝐋 𝐁𝐎𝐓𝐒", url=f"https://t.me/Emergency_Gamer"),
             InlineKeyboardButton("𝐁𝐎𝐓𝐕𝐄𝐑𝐒𝐄", url=f"https://t.me/Emergency_Gamer"),
             ],
     
              [
              InlineKeyboardButton("𝐆𝐈𝐓𝐇𝐔𝐁 𝐏𝐑𝐎𝐅𝐈𝐋𝐄", url=f"https://github.com/vicky0604hello"),
              InlineKeyboardButton("𝐕𝐈𝐂𝐊𝐘 𝐂𝐇𝐎𝐔𝐃𝐇𝐀𝐑𝐘 ♡︎", url=f"https://t.me/Emergency_Gamer"),
              ],
     
              [
              InlineKeyboardButton("𝐏𝐘𝐑𝐎𝐍𝐄", url=f"https://t.me/Emergency_Gamer"),
              InlineKeyboardButton("𝗔𝗟 𝗦𝗣𝗔𝗠 𝗕𝗢𝗧", url=f"https://t.me/Emergency_Gamer"),
              ]
       ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/5730046b13f9755ebe5bc.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
