# bot.py
import os
import discord
import re

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
TARGET_USER = os.getenv('TARGET_USER')
CURRENT_USER = os.getenv('CURRENT_USER')

POLICE_KILL_MESSAGE = f'@{CURRENT_USER} The police are here, and they\'re after you! Type'

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

def is_police_kill_message(message):
    if POLICE_KILL_MESSAGE in message.content:
        secret_message = re.search('`.*`', message.content)
        print(secret_message)

@client.event
async def on_message(message):
    is_police_kill_message(message)
#    if str(message.author) == TARGET_USER:
#        embed_list = message.embeds
#        for embed in embed_list:
#            print(embed.title)
#            print(embed.description)
client.run(TOKEN)
