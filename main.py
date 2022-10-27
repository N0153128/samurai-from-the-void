import discord
import settings
from github import Github


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/hello'):
        await message.channel.send('The void welcomes you.')
    elif message.content.startswith('/reply'):
        await message.reply('Sup', mention_author=True)


client.run(settings.TOKEN)
