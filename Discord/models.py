from django.db import models

# Model to store the DiscordUser
class DiscordUser(models.Model):
    discord_user = models.CharField(max_length=90)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.discord_user
