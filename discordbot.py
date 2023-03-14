import discord
import subprocess
from secrets_1 import DISCORD_API_KEY

permissions_int = 10256

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True
client = discord.Client(intents=intents)

prefix = "!" # Change the prefix to "!"

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print('Message received:', message.content) # Add this line to check if messages are being received by the bot

    if message.content.startswith(prefix + 'hello'): # Use the prefix variable here
        await message.channel.send('Hello!')

client.run(DISCORD_API_KEY)

