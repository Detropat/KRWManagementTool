import discord


class User:
    def __init__(self, uid, user):
        self.uid = uid
        self.user = user

    def get_user(self):
        if self.uid is None:
            print('No UID has been specificed')
            return

        self.user = DiscordUser.objects.get(discord_user=self.uid)
        
