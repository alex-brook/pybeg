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
    id = discord.utils.get(client.get_all_members(), name=CURRENT_USER.split('#')[0], discriminator=CURRENT_USER.split('#')[1]).id
    POLICE_KILL_MESSAGE = '<@' + str(id) + '> The police are here, and they\'re after you! Type'
    if POLICE_KILL_MESSAGE in message.content:
        secret_message = re.search('`.*`', message.content)
        print(secret_message)

@client.event
async def on_message(message):
    if 'The police are here' in message.content:
        print(message.content)
        is_police_kill_message(message)
#    if str(message.author) == TARGET_USER:
#        embed_list = message.embeds
#        for embed in embed_list:
#            print(embed.title)
#            print(embed.description)
client.run(TOKEN)
