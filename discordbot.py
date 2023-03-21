import discord
import subprocess
import asyncio
import os
from my_channel_id import CHANNEL_ID
from main import get_conspiracy_post
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True
client = discord.Client(intents=intents)
token = os.getenv('DISCORD_API_KEY')

prefix = "!"

async def post_conspiracy():
    await client.wait_until_ready()  # Wait until the bot is ready
    while not client.is_closed():
        channel = discord.utils.get(client.get_all_channels(), id=CHANNEL_ID) 
        conspiracy_post = get_conspiracy_post()
        await channel.send(conspiracy_post)
        await asyncio.sleep(86400)  # Delay execution for 1 day

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    client.loop.create_task(post_conspiracy())  # Start the post_conspiracy task

@client.event
async def on_message(message):
    #print('Message received:', message.content) # Add this line to check if messages are being received by the bot

    if message.content.lower().startswith(prefix + 'conspiracy'): # Use the prefix variable here
        conspiracy_post = get_conspiracy_post()
        await message.channel.send(conspiracy_post)

client.run(token)
