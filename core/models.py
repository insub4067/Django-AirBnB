from turtle import update
from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
