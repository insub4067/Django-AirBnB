from django.db import models
from core.models import TimeStampedModel

# Create your models here.


class List(TimeStampedModel):

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ManyToManyField("rooms.Room", blank=True)

    def __str__(self):
        return f"{self.user} - {self.name}"
