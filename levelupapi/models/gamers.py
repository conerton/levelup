from django.db import models
from .users import User


class Gamer(models.Model):

    bio = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
