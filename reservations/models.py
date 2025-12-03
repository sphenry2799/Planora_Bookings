from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Optional: Validators for date and time
def validate_reservation_date(value):
    if value < timezone.now().date():
        raise ValueError("Reservation date cannot be in the past.")


def validate_reservation_time(value):
    # Example: allow only reservations between 08:00 and 22:00
    if value.hour < 8 or value.hour > 22:
        raise ValueError("Reservation time must be between 08:00 and 22:00.")


class Reservation(models.Model):
    """
    Model representing a reservation in your booking service.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now, validators=[validate_reservation_date])
    time = models.TimeField(validators=[validate_reservation_time])
    guests = models.PositiveIntegerField(default=1)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ('date', 'time', 'user') 

    def __str__(self):
        return (
            f"Dear {self.name}, your booking for {self.guests} "
            f"guest(s) on {self.date} at {self.time} is confirmed."
        )