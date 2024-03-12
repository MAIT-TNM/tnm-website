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
from django.core.mail import send_mail
# Create your views here.

razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

def pay(request,name, *args, **kwargs):
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
    email = request.GET.get("email")
    print(email)
    participant = Participation.objects.get(leader_email=email, event=event)
    payment = Payments(order_id=razorpay_order_id, event_id=event.event_id, participant=participant)
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
                    payment = Payments.objects.get(order_id=razorpay_order_id)
                    payment.payment_success = True
                    # payment.participant.payment_success = True
                    payment.save()
                    send_mail(
                        "TNM confirmation",
                        f'congrats participant for successfully registering for MAIT T&M in the {payment.event.event_name} event \n'
                        f'your event will be held on {payment.event.event_date}',
                        settings.EMAIL_HOST_USER,
                        [f'{payment.participant.leader_email}']
                    )

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



