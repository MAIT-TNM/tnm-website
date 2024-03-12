from django.db import models
from Login.models import NewUser
import uuid
# Create your models here.

GENRES= (
    ("Techinical","technical"),
    ("Cultural","cultural"),
    ("Sports", "sports")
)
class Event (models.Model):
    event_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    event_name = models.CharField(max_length=20, unique=True)
    event_date = models.DateTimeField()
    event_incharge = models.CharField(max_length=20)
    event_discpription = models.TextField(null=True)
    event_genre = models.CharField(choices=GENRES, max_length=10, default="sports")
    event_photo = models.ImageField(null=True, upload_to="Home/static")
    event_incharge_contact = models.IntegerField(null=True)
    event_rules = models.TextField(null=True)
    society_name = models.CharField(null=True, max_length=25)
    entry_fees = models.IntegerField(null=True)
    prize_pool = models.IntegerField(null=True)
    def __str__(self):
        return self.event_name
class Participation(models.Model):
    p_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    # particpant_email = models.ForeignKey(NewUser,on_delete=modelps.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    # phone = models.IntegerField(null=True)
    first_name = models.CharField(max_length=20, null=True)
    second_name = models.CharField(max_length=20, null=True)
    third_name = models.CharField(max_length=20, null=True)
    fourth_name = models.CharField(max_length=20, null=True)

    first_phone = models.CharField(default="0", max_length=10)
    second_phone= models.CharField(null=True, max_length=10)
    third_phone= models.CharField(null=True, max_length=10)
    fourth_phone= models.CharField(null=True, max_length=10)

    first_college = models.CharField(max_length=40, null=True)
    second_college = models.CharField(null=True, max_length=40)
    third_college = models.CharField(max_length=40, null=True)
    fourth_college = models.CharField(max_length=40, null=True)

    team_name = models.CharField(max_length=20, null=True)
    # payment_success = models.BooleanField(default=False)
        
        
        
        
        
        
        
        

    
    



    #
    # event = Event.objects.get(event_name=name)
    # user = NewUser.objects.get(email=request.user)
    # registration = Participation(particpant_email=user, event=event, phone=user.phone)
    # registration.save()
