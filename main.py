import discord
from passwordgenerator import *
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('bye'):
        await message.channel.send(":wave:")
    elif message.content.startswith('/generatepassword'):
        await message.channel.send(sifre_uret(8))  
    elif message.content.startswith('human'):
        await message.channel.send("pizza wants a snack eee ee eee")
    else:
        await message.channel.send(message.content)

client.run("Your token here")
