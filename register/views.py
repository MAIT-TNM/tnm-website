from django.shortcuts import render,HttpResponse
from Home.models import Event, Participation
from Login.models import NewUser
from django.conf import settings
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
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
    callback_url = f'paymenthandler/{name}'


    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['rayzorpay_merchant_key'] =settings.RAZOR_KEY_ID
    context['amount'] = amount
    context["currency"] = currency
    context['callback_url'] = callback_url
    print(context)
    return render(request, 'Register.html', context=context)


@csrf_exempt
def paymenthandler(request,name):
    # only accept POST request.
    if request.method == "POST":
        try:

            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 20000  # Rs. 200
                try:

                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
                    event = Event.objects.get(event_name=name)
                    user = NewUser.objects.get(email=request.user)
                    registration = Participation(particpant_email=user, event=event, phone=user.phone)
                    registration.save()

                    # render success page on successful caputre of payment
                    return render(request, 'paymentsuccess.html')
                except:

                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:

                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except:

            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
        # if other than POST request is made.
        return HttpResponseBadRequest()