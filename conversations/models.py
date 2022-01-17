from django.db import models
import conversations
from core.models import TimeStampedModel

# Create your models here.
class Conversation(TimeStampedModel):

    """Conversation Model Definition"""

    participants = models.ManyToManyField(
        "users.User", related_name="conversations", blank=True
    )

    def __str__(self):
        return str(self.createdAt)


class Message(TimeStampedModel):

    """Message Model Definition"""

    message = models.TextField(max_length=1000)
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} : {self.message}"
