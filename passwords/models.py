from django.db import models
from django.conf import settings

class StoredPassword(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,)

    url = models.URLField(max_length=200)
    username = models.CharField(max_length=200, null=True)
    encrypted_password = models.CharField(max_length=200)
