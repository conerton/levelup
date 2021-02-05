
from django.db import models
# from django.contrib.auth.models import Events
from .gamers import Gamer
from .games import Game


class Event(models.Model):

    event_time = models.DateField.auto_now()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    scheduler = models.ForeignKey(Gamer, on_delete=models.CASCADE)
