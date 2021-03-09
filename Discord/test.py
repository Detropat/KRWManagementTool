import discord

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
    
    discord_user(message.author.id)

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

# Generic function for KRW Discord User management
def discord_user(uid):
    if uid is None:
        print('No UID has been given')
        return

    print('Handling user:',uid)ö

    user = DiscordUser.objects.get(discord_user=uid)
    print(user)
    try:
        user = DiscordUser.objects.get(discord_user=uid)
    except DoesNotExist:
        user = DiscordUser.objects.create(discord_user=uid)

client.run('ODE4NTc5MzQ5ODI0ODY0MjU2.YEaHbQ.FNhI1YYoCnctFFPMzf_mvdsefP0')
