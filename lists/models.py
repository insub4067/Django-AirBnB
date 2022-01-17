from django.db import models
from core.models import TimeStampedModel

# Create your models here.


class List(TimeStampedModel):

    name = models.CharField(max_length=80)
    user = models.ForeignKey(
        "users.User", related_name="lists", on_delete=models.CASCADE
    )
    room = models.ManyToManyField("rooms.Room", related_name="lists", blank=True)

    def __str__(self):
        return f"{self.user} - {self.name}"
