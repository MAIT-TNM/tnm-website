from django.db import models
from Login.models import NewUser
# Create your models here.
class Event (models.Model):
    event_id = models.IntegerField(primary_key=True)
    event_name = models.CharField(max_length=20, unique=True)
    event_date = models.DateTimeField()
    event_incharge = models.CharField(max_length=20)
    event_discpription = models.TextField(null=True)
    event_photo = models.ImageField(null=True, upload_to="Home/static")
    
    def __str__(self):
        return self.event_name
class Participation(models.Model):
    p_id = models.IntegerField(primary_key=True)
    particpant_email = models.ForeignKey(NewUser,on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True)
    #
    # event = Event.objects.get(event_name=name)
    # user = NewUser.objects.get(email=request.user)
    # registration = Participation(particpant_email=user, event=event, phone=user.phone)
    # registration.save()
