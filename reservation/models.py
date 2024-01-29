from django.db import models
from django.utils import timezone
from users.models import User


class Reservation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.IntegerField()
    number_of_persons = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='reservations')
    # is_table_booked = models.BooleanField(default=False)
    # confirmation_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.date} {self.time}"

    # def confirm_reservation(self):
    #     self.is_table_booked = True
    #     self.confirmation_time = timezone.now()
    #     self.save()
    #
    # def cancel_reservation(self):
    #     self.is_table_booked = False
    #     self.confirmation_time = None
    #     self.save()
    #
    # def is_reservation_expired(self):
    #     if self.confirmation_time:
    #         expiration_time = self.confirmation_time + timezone.timedelta(hours=3)
    #         return timezone.now() > expiration_time
    #     return False
    #
    # def release_table_if_expired(self):
    #      if self.is_reservation_expired() and self.is_table_booked:
    #         self.is_table_booked = False
    #         self.confirmation_time = None
    #         self.save()
