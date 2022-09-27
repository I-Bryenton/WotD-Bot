# bot.py
import os
from WordOfTheDay import getWordOfTheDay

import discord
from dotenv import load_dotenv
from discord.ext import commands
#from discord.ui import Button, View

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='/', intents=intents)

# client = discord.Client(intents=discord.Intents.default())
# or
# class CustomClient(discord.Client):
#   async def on_ready(self):
#       print(f'{self.user} has connected to Discord!')
# client = CustomClient()
# client.run(TOKEN)


@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected to the server')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

#@bot.command(name='hello')
#async def hello(ctx):
#    button = Button(label="Click me!", style=discord.ButtonStyle.green, custom_id="click_one", emoji="👌")
#    view = View()
#    view.add_item(button)
#    await ctx.send("Hi!", view=view)

# @client.event
# async def on_message(message):
#    if message.author == client.user:
#        return

#    if message.content.startswith('!'):
#        await message.channel.send('Hello!')


@bot.command(name='wotd', help='Responds with the word of the day')
async def word_of_the_day(ctx):
    wotd = getWordOfTheDay()
    await ctx.send(wotd)

# Quiz me - generates a quiz based off of words used in the past 7 days

#get wotd from dictionary.com

bot.run(TOKEN)
