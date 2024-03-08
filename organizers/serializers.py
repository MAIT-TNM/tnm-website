from rest_framework.serializers import ModelSerializer
from register.models import Payments
class PaymentsSerializer(ModelSerializer):
	class Meta:
		model = Payments
		fields = "__all__"