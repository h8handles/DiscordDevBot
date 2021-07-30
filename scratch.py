#!/bin/env python3



import discord
from discord.ext import commands
import json
import os
import time
import asyncio


#client
client = commands.Bot(command_prefix = '!')

token = 'ODY5OTMyNjA0MzExMzQzMTg1.YQFZ3w.WaGLJ-U82AmAyvpE52X0SUqpIpw'
@client.event
async def on_ready():
	print('we have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
	if message.author == client.user:

		 return 
	if message.content.startswith('!hello'):
		await message.channel.send("Hello!")
#make version command executable on all channels




#run client on server(aka BOT)
client.run(token)








