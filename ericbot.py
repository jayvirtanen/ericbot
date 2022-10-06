import time
import os
import discord
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
TOKEN = 'TOKEN'
client = discord.Client(intents=discord.Intents.default())

bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    now = datetime.now()
    sender = str(message.author)
    t = round(time.time())
    print(sender)
    print(t)
    hour = int(now.hour)%12
    if sender == 'TARGET#user' and t%2:
        await message.channel.send("Eric, it's " + str(hour).zfill(2) + ":" + str(now.minute).zfill(2))

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='ERIC')
async def yoooo(ctx):
    response = https://www.youtube.com/watch?v=MxV2u46ER9M
    await ctx.send(response)

client.run('TOKEN')
bot.run('TOKEN')

