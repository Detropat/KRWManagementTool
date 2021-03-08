import discord

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    print('Message called back: ', message.content)
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run('ODE4NTc5MzQ5ODI0ODY0MjU2.YEaHbQ.VV7iPFb5leqewiCT0dW2VzMRTs0')
