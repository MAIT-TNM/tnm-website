from django.shortcuts import render,redirect
from django.http import HttpResponse
import csv
from register.models import Payments
from rest_framework.views import APIView, Response
from Login.models import NewUser
from Home.models import Event
from .serializers import PaymentsSerializer
# Create your views here.
def EventData(request):

	if request.user.is_superuser:
		queryset = Payments.objects.filter(payment_success=True)
		data = []
		for i in queryset:
			data.append([str(i.event),str(i.participant.team_name),str(i.participant.leader_email),str(i.participant.first_phone), str(i.participant.first_name)])
			print(i)
		print(data)
		response = HttpResponse(content_type="text/csv")
		response["Content-Disposition"] = 'attachment; filename="data.csv"'
		writer = csv.writer(response)
		writer.writerow(["event name",'team_name', 'email', 'phone','leader name' ])  # Replace with actual field names
		writer.writerows(data)
		return response
	else:
		return redirect("/")

# class EventAPI(APIView):
# 	queryset = Payments.objects.filter(payment_success=True)
# 	def get(self, request, *args, **kwargs):
#
# 		serialised = PaymentsSerializer(data = queryset, many=True)
