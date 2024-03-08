from rest_framework import serializers
from .models import Event, Participation

class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = '__all__'

class ParticipationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Participation
		fields = '__all__'
