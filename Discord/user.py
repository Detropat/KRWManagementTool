import discord
import logging
from discord.models import DiscordUser


class User:
    def __init__(self, uid):
        self.uid = uid

    # Retieve a user
    def get_user(self):
        if self.uid is None:
            logger.warning('No UID has been specificed')
            return

        try:
            self.user = DiscordUser.objects.get(discord_user=self.uid)
        except DoesNotExist:
            # Doesn't exists? Create a new one
            self.user = create_user(self.uid)

        return self.user

    # Create a new user
    def create_user(self):
        if self.uid is None:
            logger.warning('No UID has been specified')
            return

        self.user = DiscordUser.objects.create(discord_user=self.uid)

        return self.user
