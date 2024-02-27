from django.shortcuts import render,redirect
from django.http import HttpResponse
import csv
from register.models import Payments
from Login.models import NewUser
from Home.models import Event

# Create your views here.
def EventData(request):

	if request.user.is_superuser:
		queryset = Payments.objects.filter(payment_success=True)
		data = []
		for i in queryset:
			data.append([str(i.event),str(i.user_id),i.user_id.phone])
			print(i)
		print(data)
		response = HttpResponse(content_type="text/csv")
		response["Content-Disposition"] = 'attachment; filename="data.csv"'
		writer = csv.writer(response)
		writer.writerow(["event name", 'email', 'phone', ])  # Replace with actual field names
		writer.writerows(data)
		return response
	else:
		return redirect("/")