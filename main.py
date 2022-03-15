import discord
import requests
import json
from weather import *

token = 'OTUzMzgxMDg2ODU4MTgyNjY3.YjDvVA.VfpJ3t1CQl1Qz_aiEA40MHZ8KVA'
api_key = 'c2d96ff66912449e996ff66912949ee1'
client = discord.Client()
command_prefix = '!weather_'

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='w.[location]'))

@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith(command_prefix):
        if len(message.content.replace(command_prefix, '')) >= 1:
            location = message.content.replace(command_prefix, '').lower()
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial'
            try:
                data = parse_data(json.loads(requests.get(url).content)['main'])
                await message.channel.send(embed=weather_message(data, location))
            except KeyError:
                await message.channel.send(embed=error_message(location))

client.run(token)
