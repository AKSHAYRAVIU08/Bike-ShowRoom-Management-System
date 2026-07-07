from django.shortcuts import render, redirect
from .models import Register,Send
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.conf import settings
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
# Create your views here.

def one(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print("username", username)
        print("email", email)
        print("password", password)
        if Register.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            Register.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Registration Successfull")
            return redirect('two')
    return render(request, 'one.html')


def two(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login Successfull")
            return redirect('three')
        else:
            messages.error(request, "Invalid Username or Password")
    return render(request, 'two.html')


def three(request):
    return render(request, 'three.html')


def four(request):
    if request.method == "POST":
        customer_name = request.POST.get("customer_name")
        district = request.POST.get("district")
        purpose = request.POST.get("purpose")
        print("customer_name", customer_name)
        print("district", district)
        print("purpose", purpose)
        if Send.objects.filter(customer_name=customer_name).exists():
            messages.error(request, "Customer Name already exists")
        else:
            Send.objects.create(customer_name=customer_name, district=district, purpose=purpose)
            messages.success(request, "Send Details Added Successfully")
            return redirect('five')
    return render(request, 'four.html')


def five(request):
    return render(request, 'five.html')


def six(request):
    return render(request, 'six.html')


def seven(request):
    return render(request, 'seven.html')


def eight(request):
    return render(request, 'eight.html')


def nine(request):
    return render(request, 'nine.html')


def ten(request):
    return render(request, 'ten.html')


def eleven(request):
    return render(request, 'eleven.html')


def twovelve(request):
    return render(request,'twovelve.html')


def thirteen(request):
    return render(request,'thirteen.html')


def fourteen(request):
    return render(request,'fourteen.html')


def fifteen(request):
    return render(request,'fifteen.html')


def sixteen(request):
    return render(request,'sixteen.html')


def seventeen(request):
    return render(request,'seventeen.html')


def payment(request):

    client = razorpay.Client(
        auth=(settings.RAZORPAY_KEY_ID,
              settings.RAZORPAY_KEY_SECRET)
    )

    payment_data = {
        "amount": 50000,   # Amount in paise = 500 INR
        "currency": "INR",
        "receipt": "order_rcptid_11"
    }

    order = client.order.create(data=payment_data)

    context = {
        'order_id': order['id'],
        'razorpay_key': settings.RAZORPAY_KEY_ID,
        'amount': payment_data['amount'],
        'currency': payment_data['currency'],
    }

    return render(request, 'payment.html', context)


@csrf_exempt
def payment_success(request):

    if request.method == "POST":

        client = razorpay.Client(
            auth=(settings.RAZORPAY_KEY_ID,
                  settings.RAZORPAY_KEY_SECRET)
        )

        params_dict = {
            'razorpay_order_id': request.POST.get('razorpay_order_id'),
            'razorpay_payment_id': request.POST.get('razorpay_payment_id'),
            'razorpay_signature': request.POST.get('razorpay_signature')
        }

        try:
            client.utility.verify_payment_signature(params_dict)
            return render(request, 'success.html')

        except:
            return HttpResponseBadRequest()