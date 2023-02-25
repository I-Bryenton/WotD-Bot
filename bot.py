# bot.py
import os
from WordOfTheDay import getWordOfTheDay

import discord
from dotenv import load_dotenv
from discord.ext import commands

# Gets the .env file values
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()

# command_prefix can be changed according to preference
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected to the server')

# Command to print out the generated word of the day
@bot.command(name='wotd', help='Using "/wotd" responds with the word of the day')
async def word_of_the_day(ctx):
    wotd = getWordOfTheDay()
    await ctx.send(wotd)

bot.run(TOKEN)
