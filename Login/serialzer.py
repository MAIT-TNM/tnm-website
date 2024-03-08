from rest_framework import serializers
from .models import NewUser
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = NewUser
		fields = ["email", "password", "phone"]
	def create(self, validated_data):
		user = NewUser.objects.create_user(**validated_data)
		return user
