import discord
import subprocess
from secrets_1 import DISCORD_API_KEY
from main import get_conspiracy_post

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True
client = discord.Client(intents=intents)

prefix = "!"

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print('Message received:', message.content) # Add this line to check if messages are being received by the bot

    if message.content.lower().startswith(prefix + 'conspiracy'): # Use the prefix variable here
        conspiracy_post = get_conspiracy_post()
        await message.channel.send(conspiracy_post)

client.run(DISCORD_API_KEY)

