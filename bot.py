#!/usr/bin/env python3
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

def get_user(username):
    return discord.utils.get(client.get_all_members(), name=username.split('#')[0], discriminator=username.split('#')[1])

def is_balance_message(message):
    if not message.embeds:
        return False

    username = CURRENT_USER.split('#')[0] 
    balance_title = f'{username}\'s balance'
    return balance_title in message.embeds[0].title 

def get_wallet_total(balance_message):
    embed_msg = balance_message.embeds[0].description
    result = re.search('\*\*Wallet\*\*: (.*)\n', embed_msg).group(1)
    return int(result.replace(',',''))

def is_police_message(message):
    id = get_user(CURRENT_USER).id
    return '<@' + str(id) + '> The police are here, and they\'re after you! Type' in message.content

def get_police_secret(message):
    return re.search('`.*`', message.content).group(1)

@client.event
async def on_message(message):
    if is_police_message(message):
        print("We found a police message")
        print(get_police_secret(message))
    elif is_balance_message(message):
        print("We found a balance message")
        print(f'current user has {get_wallet_total(message)} coins')
#    if str(message.author) == TARGET_USER:
#        embed_list = message.embeds
#        for embed in embed_list:
#            print(embed.title)
#            print(embed.description)
client.run(TOKEN)
