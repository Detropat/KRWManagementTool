import discord
from discord import User

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    # Ignore the messages from the bot itself
    if message.author == client.user:
        return

    # Find out if we recognize this user from previous sessions, thus it needs to be in our own database
    # If it doesn't exists, create the user for tracking it's unique ID
    user = User()
    user.get_user(message.author.id)

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

client.run('ODE4NTc5MzQ5ODI0ODY0MjU2.YEaHbQ.0ZqJhBKtiiV-adnJk8-5nef5PnE')
