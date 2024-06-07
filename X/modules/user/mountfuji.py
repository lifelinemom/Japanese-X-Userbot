#MIT License

#Copyright (c) 2024 Japanese-X-Userbot

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


import random
from pyrogram import Client, filters
from config import SUDO_USERS
from .help import * 

hl = "."

@Client.on_message(
    filters.command(["fuji"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def castle(client, message):
    args = message.text.split(" ")[1:]
    castledata = [
  "https://graph.org/file/35424f110fac7acfad730.jpg",
  "https://graph.org/file/62dc1c72a59522fd61000.jpg",
  "https://graph.org/file/e76dcebdce2c126b682cd.jpg",
  "https://graph.org/file/bbaaf348c363ae0167ef4.jpg",
  "https://graph.org/file/0008dc21964d360b0ca20.jpg",
  "https://graph.org/file/166efa15e7559440e11fb.jpg",
  "https://graph.org/file/da1fb683140e9d5eb79b2.jpg",
  "https://graph.org/file/62dc1c72a59522fd61000.jpg",
    ]
    castle_url = random.choice(castledata)
    await message.reply_photo(castle_url)

add_command_help(
    "•─╼⃝𖠁 Mᴏᴜɴᴛ Fᴜᴊɪ",
    [
       ["fuji", "Gɪᴠᴇ random Mᴏᴜɴᴛ Fᴜᴊɪ pic."],
        ],
)
