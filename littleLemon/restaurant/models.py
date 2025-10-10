from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.title

class Booking(models.Model):
    name = models.CharField(max_length=100)
    number_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()

    def __str__(self):
        return f"Booking for {self.name} on {self.BookingDate}"