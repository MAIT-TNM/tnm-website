from django.db import models
from Login.models import NewUser
from Home.models import Event
# Create your models here.
class Payments(models.Model):
	order_id = models.CharField(max_length=40, primary_key=True)
	user_id = models.ForeignKey(NewUser,on_delete=models.CASCADE)
	event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
	payment_success = models.BooleanField(default=False)