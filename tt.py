from telethon import TelegramClient, events, sync
import re
from time import sleep
apd = 5706121
aph = 'feaa35ddd9bf15e761de280218c9d7fd'


channel_username = "kllllllwowo"
def sas():
	app =  TelegramClient('session_name', api_id=apd,api_hash=aph)
	app.start()
	for i in range(591):
		app.send_message(channel_username,"فلوس")
		sleep(1)
		for message in app.get_messages(channel_username, limit=4):
			try:
				for message in app.get_messages(channel_username, limit=10):
					
					aaa = re.findall(r'\d+', message.message)
					
					print(aaa)
					sleep(1)
					app.send_message(channel_username,f"استثمار {aaa[0]}")
					app.send_message(channel_username,"جيد")
					sleep(3000)
			except:
				pass
sas()
