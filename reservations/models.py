from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Reservation(models.Model):
    """
    Represents a reservation for a specific resource.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    time = models.TimeField()
    guests = models.PositiveIntegerField(default=1)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ('resource', 'date', 'time')
        ordering = ['date', 'time']

    def __str__(self):
        return f'{self.name} - {self.date} {self.time} ({self.resource})'
