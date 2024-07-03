import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess

import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN, WEBHOOK, PORT
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput
from aiohttp import web

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Initialize the bot
bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Define aiohttp routes
routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("https://text-leech-bot-for-render.onrender.com/")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

async def start_bot():
    await bot.start()
    print("Bot is up and running")

async def stop_bot():
    await bot.stop()

async def main():
    if WEBHOOK:
        # Start the web server
        app_runner = web.AppRunner(await web_server())
        await app_runner.setup()
        site = web.TCPSite(app_runner, "0.0.0.0", PORT)
        await site.start()
        print(f"Web server started on port {PORT}")

    # Start the bot
    await start_bot()

    # Keep the program running
    try:
        while True:
            await asyncio.sleep(3600)  # Run forever, or until interrupted
    except (KeyboardInterrupt, SystemExit):
        await stop_bot()
    
@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text(
       f"**ℍ𝔼𝕃𝕃𝕆** ❤️\n\n◆〓◆ ❖ 🇵 🇦 🇹 🇭 🇦 🇳  🇸 🇮 🇷  ❖ ™ ◆〓◆\n\n❈  𝕀 𝔸𝕞 𝔸 𝔹𝕆𝕋 𝔽𝕠𝕣 𝔻𝕠𝕨𝕟𝕝𝕠𝕒𝕕 𝕃𝕚𝕟𝕜𝕤 𝔽𝕣𝕠𝕞 𝕐𝕠𝕦𝕣 .𝐓𝐗𝐓 𝔽𝕚𝕝𝕖 𝔸𝕟𝕕 𝕋𝕙𝕖𝕟 𝕌𝕡𝕝𝕠𝕒𝕕 𝕋𝕙𝕒𝕥 𝔽𝕚𝕝𝕖 𝕆𝕟 𝕋𝕖𝕝𝕖𝕘𝕣𝕒𝕞. 𝕊𝕠 𝔹𝕒𝕤𝕚𝕔𝕒𝕝𝕝𝕪 𝕀𝕗 𝕐𝕠𝕦 𝕎𝕒𝕟𝕥 𝕋𝕠 𝕌𝕤𝕖 𝕄𝕖 𝔽𝕚𝕣𝕤𝕥 𝕊𝕖𝕟𝕕 𝕄𝕖  ➪ /pathan ℂ𝕠𝕞𝕞𝕒𝕟𝕕 𝔸𝕟𝕕 𝕋𝕙𝕖𝕟 𝔽𝕠𝕝𝕝𝕠𝕨 𝔽𝕖𝕨 𝕊𝕥𝕖𝕡𝕤...", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✜ 🇵 🇦 🇹 🇭 🇦 🇳 ✜" ,url=f"https://t.me/ALTAFPATHAN") ],
                    [
                    InlineKeyboardButton("✜ **ℙ𝔸𝕋ℍ𝔸ℕ** ✜" ,url="https://t.me/ALTAFPATHAN") ],
                    [
                    InlineKeyboardButton("🦋 🇵 🇦 🇹 🇭 🇦 🇳  🦋" ,url="https://t.me/ALTAFPATHAN") ]                               
            ]))


@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("♦ 🇸 🇹 🇴 🇵  ♦", True)
    os.execl(sys.executable, sys.executable, *sys.argv)



@bot.on_message(filters.command(["pathan"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text('** 𝕊𝔼ℕ𝔻 𝕐𝕆𝕌ℝ 🇹 🇪 🇽 🇹  𝔽𝕀𝕃𝔼 ** ⏍')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"
    
    try:
       with open(x, "r") as f:
           content = f.read()
       content = content.split("\n")
       links = []
       for i in content:
           links.append(i.split("://", 1))
       os.remove(x)
            # print(len(links)
    except:
           await m.reply_text("**𝕀ℕ 𝕍𝔸𝕃𝕀𝔻 𝕋𝕏𝕋 𝔽𝕀𝕃𝔼.** ☹️")
           os.remove(x)
           return
    
   
    await editable.edit(f" ** 𝕋𝕆𝕋𝔸𝕃 𝕃𝕀ℕ𝕂𝕊 𝔽𝕆𝕌ℕ𝔻 𝔸ℝ𝔼 🔗** **{len(links)}**\n\n**𝕎ℍ𝔼ℝ𝔼 𝕐𝕆𝕌 𝕎𝔸ℕ𝕋 𝕋𝕆  𝕊𝕋𝔸ℝ𝕋 𝔻𝕆𝕎ℕ𝕃𝕆𝔸𝔻𝕀ℕ𝔾** **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**ℕ𝕆𝕎 ℙ𝕃𝔼𝔸𝕊𝔼 𝕊𝔼ℕ𝔻 𝕄𝔼 𝕐𝕆𝕌ℝ 🇧 🇦 🇹 🇨 🇭  ℕ𝔸𝕄𝔼 ** ")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    

    await editable.edit(" **𝔼ℕ𝕋𝔼ℝ 𝕋ℍ𝔼 🇷 🇪 🇸 🇴 🇱 🇺 🇹 🇮 🇴 🇳 𝔽𝕆ℝ 𝕐𝕆𝕌ℝ 𝕍𝕀𝔻𝔼𝕆 ℚ𝕌𝔸𝕃𝕀𝕋𝕐**  🎬\n☞ **144,240,360,480,720,1080**\n**ℙ𝕃𝔼𝔸𝕊𝔼 ℂℍ𝕆𝕆𝕊𝔼 ℚ𝕌𝔸𝕃𝕀𝕋𝕐** ")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    
    

    await editable.edit("✏️ ℕ𝕆𝕎 𝔼ℕ𝕋𝔼ℝ 𝔸 🇨 🇦 🇵 🇹 🇮 🇴 🇳 𝕋𝕆 𝔽𝕆ℝ 𝔸𝔻𝔻 ℂ𝔸ℙ𝕋𝕀𝕆ℕ 𝕆ℕ 𝕐𝕆𝕌ℝ 𝕌ℙ𝕃𝕆𝔸𝔻𝔼𝔻 𝔽𝕀𝕃𝔼.** ")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    highlighter  = f"️ ⁪⁬⁮⁮⁮"
    if raw_text3 == 'Robin':
        MR = highlighter 
    else:
        MR = raw_text3
   
    await editable.edit("🌄 **ℕ𝕆𝕎 𝕊𝔼ℕ𝔻 𝔸 🇹 🇭 🇺 🇲 🇧  𝕌ℝ𝕃 **\n**𝔽𝕆ℝ 𝔼𝕏𝔸𝕄ℙ𝕃𝔼** » https://graph.org/file/a1ab55d1432fcab0cfc0e.jpg\n\n **𝕆ℝ 𝕀𝔽 𝔻𝕆ℕ'𝕋 𝕎𝔸ℕ𝕋 𝕋ℍ𝕌𝕄𝔹ℕ𝔸𝕀𝕃 𝕊𝔼ℕ𝔻 🇳 🇴  ** = 𝐍𝐨")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):

            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url:
             url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0'}).json()['url']

            elif '/master.mpd' in url:
             id =  url.split("/")[-2]
             url =  "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:  
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
            except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
            else:
                    Show = f"❊⟱ 🇩 🇴 🇼 🇳 🇱 🇴 🇦 🇩 🇮 🇳 🇬  ⟱❊ »\n\n📝 🇳 🇦 🇲 🇪  » `{name}\n⌨ 🇶 🇺 🇦 🇱 🇮 🇹 🇾  » {raw_text2}`\n\n**🔗 𝐔𝐑𝐋 »** `{url}`"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

    except Exception as e:
                await m.reply_text(
                    f"👺 🇩 🇴 🇼 🇳 🇱 🇴 🇦 🇩 🇮 🇳 🇬  🇫 🇦 🇮 🇱 👺\n{str(e)}\n⌘ 𝐍𝐚𝐦𝐞 » {name}\n⌘ 𝐋𝐢𝐧𝐤 » `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("✅ 🇩 🇴 🇳 🇪  🇵 🇦 🇹 🇭 🇦 🇳  🇸 🇮 🇷 ")

print("""
█░█░█ █▀█ █▀█ █▀▄ █▀▀ █▀█ ▄▀█ █▀▀ ▀█▀     ▄▀█ █▀ █░█ █░█ ▀█▀ █▀█ █▀ █░█   ░ █▀▀
▀▄▀▄▀ █▄█ █▄█ █▄▀ █▄▄ █▀▄ █▀█ █▀░ ░█░     █▀█ ▄█ █▀█ █▄█ ░█░ █▄█ ▄█ █▀█   ▄ █▄█""")
print("""✅ 𝐃𝐞𝐩𝐥𝐨𝐲 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅""")
print("""✅ 𝐁𝐨𝐭 𝐖𝐨𝐫𝐤𝐢𝐧𝐠 ✅""")

bot.run()
if __name__ == "__main__":
    asyncio.run(main())
