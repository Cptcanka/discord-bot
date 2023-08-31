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
    elif message.content.startswith('human'):
        await message.channel.send("pizza wants a snack eee ee eee")
    else:
        await message.channel.send(message.content)

client.run("your token here")
