from django.db import models
# from .events import Event
# from .gamers import Gamer


class eventGamer(models.Model):

    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
