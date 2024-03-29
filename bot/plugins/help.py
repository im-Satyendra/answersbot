from cgi import parse_header
from http import client
from pydoc import cli
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from bs4 import BeautifulSoup
from bot import COMMM_AND_PRE_FIX, HELP_COMMAND
from bot.bot import Bot

import requests
import os
from urllib.parse import urlparse
import time
import gspread
import requests
import psutil
import urllib.parse
import urllib3, shutil
c = urllib3.PoolManager()

credentials = {
  "type": "service_account",
  "project_id": "gdriveuserge",
  "private_key_id": "bc3247c8d7fe901a4d9a76c915abc1b06e9c3128",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDLasLp57ad3KuZ\nOSdtx76sH8q4eTvpp/9JSa8iD5GivZA8/iRQrFeQyJ77PdkCcr52Igy1Bw9OthT0\nbTsqGmY3vo1DEKt+n5TAHSU5jsJz61TQzMwDq3eY2IUdwUU/j7LTEaoOaqIzCjcC\noWImWIH1kM8eWRMgKjGU6QdE5LYyV0LE/7wmZGrLzggGlDELzvz6v5psnPXu9ffA\n02DmgDD4UbT9HA1IR4oidySlVIlelbH0kSHDgH1+B7DApc1xjNXPggIuERKFdkyy\nBR5d5Wkms2pY+aGNQnWQpfITd1TjgDd5FbxffjnpIb36CU6J9JaNoaMJZRczRfAV\n23hT5C7RAgMBAAECggEAAbcCMqed7gHEvpNxRicnb9sKwfhfrW4ZpFwHKnHYJ/eS\nJjl8Q+PYDyPp1zNjx3YBLgzGb6ZCFkdJsO/UzluPnguwtC6JS5V70wzL2grej8yd\nl+8KD0PcS8ETijctZsZG2ymsddenS2fcI90Jb0pSuifA30Af/abtaRR317hX4t++\nmtT27MqVSdkmSvNanakrrXI5zyiNymzXxfWt7muH2ie5/SLJ7iDcq8N90wpzvEFG\nGgBwt/ZGbJIPlBwXnP0pHzzA9peAjDVhGieqNl/WO68s9IZMhNfBB6Fj/Kldhrsq\nPzBxnmAkwQLFoh5dINhvBKXxVE8SnecR3vBUAsE++QKBgQDl4AxHzoX6Q3ZtDBW+\ncKcMLTLKZbNerQWScz0500174eFoiUViMzjZmVUsxQbHoYBy9ARY9IFHuauQku5x\ndQIYW1bZ//UZix87HpEdmidmnjgOKUkmKOPQibxdmlc27ADLPRh8rOVjM65nYTlB\naDcfKKkz37UsdkgRHCa8lbkCLQKBgQDiiPG2txVPNAqfzBdSZYGsZ6h+w1O4oN0T\nJnScQYzvJtngF7w6EEncCD8eUbIs6GbcpQTr1i6GOsCabGu673D5CpUrug54iGPm\nAV/opv3m9ECukc0wfuLCCjFYNrQR4AKPhC7qhnUZ0qEkmyF8eFuICXoupA55dgNN\n8YFTOCRZtQKBgB3KLC0+EVS+W2GEWGkGlk9YqCVciqMxTvCMqJmOzZLJUfnHGEvC\nkZJ5cXVMzzUds9Sx1MJmZT6TTC1/LRFc9XmMlLPJnMzDn7d8nZe1e3er9122cflV\nATjsMJH8x2KhsPSlpT+69Dsn3mkdS1szkzkhftPvIL5zUaGOAWMdEA29AoGBAKYb\nUlnu/4IXH98ycLtrUN1RGNzybtZHpjNflEvrSOMncsT9wng072OW7GlX8DU7qAkM\nO4KOh4jHVeklrQzie80w9Fae0/OP1uiVg3T91dleqnsW0AVKVQ2BGdOcMQeWYWpI\nu3oeY4kuyBgmZDR3sG4cvOmsRCzN2vhxKKoT1ZutAoGAa1Bvzdhpx1DzhzkTuCcv\nM2NmmZ1/4m1DzVngPCBhtkrKYwPQY7Dq6gmc40udnBV/GRfI365RpQqKcUGNA/jw\nBdrxkPmYgG1M45vcCNV/FzkFPE+9EDiET92UrcgQavKwPkFfLbhWt/IdRQ6SdvZG\nZa8vm7hTF9xa6DCMtFhN/1g=\n-----END PRIVATE KEY-----\n",
  "client_email": "satuserge@gdriveuserge.iam.gserviceaccount.com",
  "client_id": "102675144284628656477",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/satuserge%40gdriveuserge.iam.gserviceaccount.com"
}
sa = gspread.service_account_from_dict(credentials)
si = "1Iuz971A-HmOQBf3y005XBO3XCEpsJZly2GL8Cc6Gar0"
sh = sa.open_by_key(si)
worksheet_list = sh.worksheets()
l = sh.worksheet("JEE ULTIMATE")
access_token = sa.auth.token
fields = "sheets(data(rowData(values(hyperlink))))"
disk = psutil.disk_usage("/").percent
free = psutil.disk_usage(".").free/100000000
bot_start_time = time.time()
def get_readable_time(seconds: int) -> int:
    """Get Time So That Human Can ReadIt"""
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time
@Bot.on_message(
    filters.command("sheet", COMMM_AND_PRE_FIX)
)
async def sheet(client: Bot, message: Message):
    await message.reply_text("https://ourclg.tech/sheet.php",disable_web_page_preview=True)

    
@Bot.on_message(
    filters.command("start")
)
async def start(client: Bot, message: Message):
    txt = message.text
    if " " in txt:
        try:
            link = txt.split(" ", 1)[1]
            cellRange = link #str(input("id?"))  # Please set the range with A1Notation. In this case, the hyperlink of the cell "A1" of "Sheet1" is retrieved.
#val = l.acell(cellRange).value

# 1. Retrieve the access token.
            access_token = sa.auth.token

# 2. Requst to the method of spreadsheets.get in Sheets API using `requests` module.
            fields = "sheets(data(rowData(values(hyperlink))))"
            url = "https://sheets.googleapis.com/v4/spreadsheets/" + si + "?ranges=" + urllib.parse.quote(cellRange) + "&fields=" + urllib.parse.quote(fields)
            res = requests.get(url, headers={"Authorization": "Bearer " + access_token})

# 3. Retrieve the hyperlink.
            obj = res.json()
#print(obj)
            ob = obj["sheets"][0]['data'][0]['rowData'][0]['values'][0]['hyperlink']
            obf= ob.replace("vid.ourclg.tech","cc.cplas.workers.dev")
         #await c.send_video(q.from_user.id, video=ob)
         #await c.send_document(q.from_user.id, document=ob, )
            mss = await client.send_message(message.chat.id,"Getting Data..")
            
            lk = obf
            fn=lk.split('/')[-1]
            filename = fn
            await mss.edit_text("Downloading!")
            with c.request('GET', lk, preload_content=False) as res, open(filename, 'wb') as out_file:
              shutil.copyfileobj(res, out_file)
            await mss.edit_text("Uploading!")
            dc = await client.send_document(message.chat.id,fn)
            await mss.delete()
            fwd = await client.forward_messages(-1001579836800, message.from_user.id,dc.message_id)
            idxkk = """
            {}
            {}
            {}"""
            k = idxkk.format(fn,message.from_user.mention,message.from_user.id)
            btnk = InlineKeyboardMarkup([[InlineKeyboardButton(text='here', url='https://t.me/c/1579836800/{}'.format(fwd.message_id))]])
            await client.send_message(-1001579836800,k,parse_mode="html",reply_markup=btnk)
            

            
        except Exception as e:
            if e == 'rowData':
                await mss.edit_text("No links found in your requested box")
            else:
                await client.send_message(-1001579836800, e)
    else:
        B = InlineKeyboardMarkup([[InlineKeyboardButton(text='Sheets', url='https://ourclg.tech/s.php')]])
        DEFAULT_START_TEXT = (
        "Hi. ☺️\n"
        "Thank you for using me.\n\n"
        "This is abot to contact admins! \n\n\n"
        "Google Sheets Link -> /sheet \n\n\n"
        "**Rules for using this bot:\n\n** "
        "1. Ask your question Directly \n"
        "2. dont edit or delete messages\n"
        "3. **Dont Spam!** \n\n\n"
        "New Features Will Come bu for next batch.\n"
        "ℹ️ Thanks 😍 for using this bot❗️❣️\n"
        "UPTIME: {}\n"
        "Disk: {}, Free: {}"
         )
        ut=get_readable_time((time.time() - bot_start_time))
        await message.reply_text(DEFAULT_START_TEXT.format(ut,disk,free),reply_markup=B, parse_mode="md") 

    
@Bot.on_message(
    filters.command("get", COMMM_AND_PRE_FIX)
)
async def grt(c,m):
   if " " in m.text:
    try:
        fur = m.text
        id = fur.split(" ", 1)[1]
        k = await m.reply_text(
            id,
            quote=True)
        cellRange = id #str(input("id?"))  # Please set the range with A1Notation. In this case, the hyperlink of the cell "A1" of "Sheet1" is retrieved.
#val = l.acell(cellRange).value

# 1. Retrieve the access token.
        access_token = sa.auth.token

# 2. Request to the method of spreadsheets.get in Sheets API using `requests` module.
        fields = "sheets(data(rowData(values(hyperlink))))"
        url = "https://sheets.googleapis.com/v4/spreadsheets/" + si + "?ranges=" + urllib.parse.quote(cellRange) + "&fields=" + urllib.parse.quote(fields)
        res = requests.get(url, headers={"Authorization": "Bearer " + access_token})

# 3. Retrieve the hyperlink.
        obj = res.json()
#print(obj)
        ob = obj["sheets"][0]['data'][0]['rowData'][0]['values'][0]['hyperlink']
        hn = l.acell(id).value
        knn = """
**Name: ** `{}`
**Url : ** `{}?a=view`"""
        btnn = InlineKeyboardMarkup([[InlineKeyboardButton(text='Download to Telegram', url='t.me/Jee_Ultimate_2022_Bot?start='+cellRange), InlineKeyboardButton(text='Watch Online', url=ob+"?a=view")]])
       
        await k.edit_text(knn.format(hn,ob), parse_mode="md", reply_markup=btnn)
    except Exception as e:
            await k.edit_text("Error: please follow pattern explained in /help .")
            await c.send_message(-1001579836800, e)
   else :
        await m.reply_text("Error: please follow pattern explained in /help .")
@Bot.on_message(filters.command("restart"))
async def rest(c,m):
    k = await m.reply_text("restarting..")
    await Client.restart(Client,True)
    await k.edit_text("restarted /start")