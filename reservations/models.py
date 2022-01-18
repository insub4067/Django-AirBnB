from django.db import models
from django.utils import timezone
from core.models import TimeStampedModel

# Create your models here.
class Reservation(TimeStampedModel):

    """Reservation Model Definition"""

    # STATUS
    PENDING = "pending"
    CANCELED = "canceled"
    CONFIRMED = "confirmed"

    STATUS_CHOICES = (
        (PENDING, "Pending"),
        (CANCELED, "Canceled"),
        (CONFIRMED, "Confirmed"),
    )

    status = models.CharField(choices=STATUS_CHOICES, max_length=15, default=PENDING)
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reservations", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.room} - {self.check_in}"

    def in_progress(self):
        current_date = timezone.now().date()
        return self.check_in <= current_date and current_date <= self.check_out

    def is_finished(self):
        current_date = timezone.now().date()
        return current_date > self.check_out
