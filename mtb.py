from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class mtb(object):
  
  START_TXT = """
  
<b>Hello {},👋
=>I Can Rename Files With Permanant Thumbnail Support 💥

=>I Can Convert Files Too 🙂

Use help Button For More Details

🧨Devoloped & Maintained By : : <a href='https://bit.ly/3gwsct3'>✯°• Yogesh R •°✯</a></b>\n
  """
  HELP_TXT = """
  
  **Hey 🙋‍♂️It's Not Complicated To Use Me.

➩ Send Me A Image To Save It As Custom Thumbnail permanently [ Optional ]

➩ Then Send Me Your File Or Video Which You Want To Rename. 

➩ Reply With File That File /rename [ Custom File Name ]

➩ Then Wait For Sometime Until Bot Renames & Upload It..!! 

<\ Available Commands />
• /start - 🎉 Start Message
• /rename - 🌊Rename Telegram Files
• /showthumb - 🎆 To Saved Custom Permanent thumbnail
• /delthumb - ❌  Clears Saved Custom Thumbnail To Default

🎉Powerded By : @YogeshBots**
"""
  
  ABOUT_TXT = """
  
<b>🎆My Name : <a href='https://t.me/YBRenameBot'>YB Rename Bot</a></b>\n
<b>👩‍🦽Version : <a href='https://t.me/YBRenameBot'>0.9.2 beta</a></b>\n
<b>⛑Subscribe : <a href='https://bit.ly/3y3Ej6u'>Click Here</a></b>\n
<b>⚙️Server : <a href='https://heroku.com'>Heroku</a></b>\n
<b>🛡Library : <a href='https://github.com/pyrogram'>Pyrogram 1.2.8</a></b>\n
<b>🪓Language : <a href='https://www.python.org'>Python 3.9.4</a></b>\n
<b>🎉Developer : <a href='https://bit.ly/3gwsct3'>✯°• Yogesh R •°✯</a></b>\n
<b>🚀Channel : <a href='https://t.me/YogeshBots'>𝗬𝗼𝗴𝗲𝘀𝗵 𝗕𝗼𝘁𝘀</a></b>\n
"""
  
  START_BUTTONS = InlineKeyboardMarkup(
    [[
      InlineKeyboardButton("👦🏻 𝑴𝒚 𝑭𝒂𝒕𝒉𝒆𝒓", url="https://t.me/YogeshBots"),
      InlineKeyboardButton("⚙️ 𝑯𝒆𝒍𝒑", callback_data="help")
     ],[
      InlineKeyboardButton("𝑨𝒃𝒐𝒖𝒕 📕", callback_data="about"),
      InlineKeyboardButton("𝑪𝒍𝒐𝒔𝒆 🔐", callback_data="close")
    ]]
    )
      
  HELP_BUTTONS = InlineKeyboardMarkup(
    [[
      InlineKeyboardButton("🔙 𝑩𝒂𝒄𝒌", callback_data="home"),
      InlineKeyboardButton("𝑪𝒍𝒐𝒔𝒆 🔐", callback_data="close")
    ]]
    )
  
  ABOUT_BUTTONS = InlineKeyboardMarkup(
    [[
      InlineKeyboardButton("🔙 𝑩𝒂𝒄𝒌", callback_data="home"),
      InlineKeyboardButton("𝑪𝒍𝒐𝒔𝒆 🔐", callback_data="close")
    ]]
    )
  
