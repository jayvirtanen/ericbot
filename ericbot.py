import time
import os
import random
import random
import discord
from dotenv import load_dotenv

from datetime import datetime

load_dotenv()
TOKEN = ''
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    now = datetime.now()
    sleep = random.randrange(3600)
    sender = str(message.author)
    t = round(time.time())
    print(sender)
    print(t)
    hour = int(now.hour)%12
    if sender == 'TARGET#user' and t%2:
        await message.channel.send("Eric, it's " + str(hour).zfill(2) + ":" + str(now.minute).zfill(2))

client.run('TOKEN')
