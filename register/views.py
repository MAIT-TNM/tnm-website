from django.shortcuts import render,HttpResponse, redirect
from django.http import JsonResponse
from Home.models import Event, Participation
from Login.models import NewUser
from django.conf import settings
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
import urllib.parse
import requests
import json
from .models import Payments
# Create your views here.

razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

def pay(request,name):
    currency = 'INR'
    amount = 100

    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))

    razorpay_order_id = razorpay_order['id']
    callback_url = f"http://localhost:8000{urllib.parse.quote(f'/paymenthandler/{name}')}"
########################################################################################################################
    # callback_url = 'paymenthandler'
    event = Event.objects.get(event_name=name)
    payment = Payments(order_id=razorpay_order_id, event_id=event.event_id)
    payment.save()
########################################################################################################################

    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['key'] = "rzp_test_lgXnrlnr3w35wr"
    context['amount'] = amount
    context["currency"] = currency
    context['callback_url'] = callback_url
    context['secret'] = settings.RAZOR_KEY_SECRET
    print(context)
    return JsonResponse(json.dumps(context), safe=False)


@csrf_exempt
def paymenthandler(request,name):
    # only accept POST request.
    if request.method == "POST":


        # get the required parameters from post request.
        payment_id = request.POST.get('razorpay_payment_id', '')
        razorpay_order_id = request.POST.get('razorpay_order_id', '')
        signature = request.POST.get('razorpay_signature', '')
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature,
        }
        # requests.post("http://localhost:5000/Regi/", data=params_dict)
        # verify the payment signature.
        result = razorpay_client.utility.verify_payment_signature(
            params_dict)
        # return redirect("/")
        if result is not None:
            amount = 100  # Rs. 200
            try:
        #
                # capture the payemt
                razorpay_client.payment.capture(payment_id, amount)
                try:
                    # print(request.user)
                    # event = Event.objects.get(event_name=name)
                    # user = NewUser.objects.get(email=str(request.user))
                    # registration = Participation(particpant_email=user, event=event, phone=user.phone)
        #             # registration.save()
                    payment = Payments.objects.get(order_id=razorpay_order_id)
                    payment.payment_success = True
                    payment.participant.payment_success = True
                    payment.save()

                    # print(payment.id)
                    return redirect("/")
                except Exception as e:
                    print(e)
                    return HttpResponseBadRequest
        #         print("success")
        #         # render success page on successful caputre of payment
        #         return redirect('/')
            except:
                print("failure")
        #         # if there is an error while capturing payment.
                return redirect(f'/Register/{name}')
        # else:
        #
        #     # if signature verification fails.
        #     return redirect(f'/Register/{name}')



