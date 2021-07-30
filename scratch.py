#!/bin/env python3



import discord
from discord.ext import commands
import json
import os
import time
import asyncio


#client
client = commands.Bot(command_prefix = '!')

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


@client.event
async def on_ready():
	print('we have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
	if message.author == client.user:

		 return 
	if message.content.startswith('!hello'):
		await message.channel.send("Hello!")
#check if a memeber joined then hopefully tell that user hello or some stats 
'''
@client.event
async def on_member_join()

'''
token = read_token()

# client on server(aka BOT)
client.run(token)








