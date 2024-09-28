from django.db import models
from .custom_user import User
# Create your models here.

class Ticket(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    train_name=models.CharField(max_length=50)
    departure_time=models.DateTimeField()
    seat_number=models.CharField(max_length=10)
    is_confirmed=models.BooleanField(default=False)
    