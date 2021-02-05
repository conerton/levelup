from django.db import models
from django.contrib.auth.models import Games


class gameType(models.Model):

    label = models.CharField(max_length=50)
