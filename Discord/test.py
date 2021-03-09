import discord

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # print('Message called back:', message.content, 'coming from', message.channel)

    if message.channel.name == 'reservations-wednesday':
        channel = message.channel
        # print('Great, this message is coming from the reservations channel')
        await channel.send(f'Thank you, {message.author.name}, we will process your reservation!')
        if message.content.startswith('$reserve'):
            print('Someone is trying to reserve', message.content)
        elif message.content.startswith('$unreserve'):
            print('Unreserving nation', message.content)
        else:
            print('Not much happening')


client.run('ODE4NTc5MzQ5ODI0ODY0MjU2.YEaHbQ.bUmDG--0HZH1TA_0KQl96_gImIc')
