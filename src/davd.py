import os
import asyncio
import youtube_dl
import discord
import configparser

ydl = youtube_dl.YoutubeDL({
        'format' : 'bestvideo+bestaudio',
        'outtmpl': '/video/%(title)s'
    })
client = discord.Client()
config = configparser.ConfigParser()
config.read('/config/setting.ini')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-dl'):
        links = message.content.split()[1::]
        await download(links, message)

async def download(links, message):
    await message.add_reaction('🌑')
    for link in links:
        with ydl:
           ydl.extract_info(link, download=True)
    await message.remove_reaction('🌑', client.user)
    await message.add_reaction('🌕')
client.run(config['DISCORD']['token'])

