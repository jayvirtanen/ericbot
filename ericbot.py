import time
import discord
from discord.ext import commands
from datetime import datetime


intents = discord.Intents.all()
intents.members = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='..')
async def yoooo(ctx):
    response = 'https://www.youtube.com/watch?v=MxV2u46ER9M'
    await ctx.send(response)

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    now = datetime.now()
    sender = str(message.author)
    t = round(time.time())
    print(sender)
    print(t)
    hour = int(now.hour)%12
    if sender == 'USERNAME' and t%2:
        await message.channel.send("Eric, it's " + str(hour).zfill(2) + ":" + str(now.minute).zfill(2))

bot.run('TOKEN')

