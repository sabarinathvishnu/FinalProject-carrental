from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


from backend.models import VehicleDb
from carapp.models import Contactdb, Bookingdb, signupdb, product
# email verification code
from django.contrib import messages
from django.core.mail import send_mail,BadHeaderError
from django.shortcuts import render, redirect
from django.conf import settings
# from carapp.templates.subscriptions.forms import SubscribeForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm,LoginForm
from django.views.generic import View
from django.http import HttpResponse




# Create your views here.

def index(request):
    cars=VehicleDb.objects.all()
    return render(request,"index.html",{"cars":cars})

def aboutpage(request):
    return render(request,"about.html")

def servicepage(request):
    return render(request,"services.html")

def carpage(request):
    global title
    if 'term' in request.GET:
        qs = product.objects.filter(title_icontains=request.GET.get('term'))
        title = list()
        for product in qs:
            title.append(product.title)
        return JsonResponse(title,safe=False)

    
    search=request.POST.get("search")
    if search is None:
        cars = VehicleDb.objects.all()
    else:
        cars=VehicleDb.objects.filter(VehicleName__istartswith=search)
    return render(request,"car.html",{'cars':cars})


def contactpage(request):
    return render(request,"contact.html")

def save_contact(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        sub = request.POST.get('subject')
        mes = request.POST.get('message')
        obj = Contactdb(name=na,email=em,subject=sub,message=mes)
        obj.save()
        return redirect(contactpage)


def cardetails(request,cid):
    cars = VehicleDb.objects.get(id=cid)
    return render(request,"cardetails.html",{'cars':cars})


# Booknow option inside car page
def booknow(request, cid):
    user = request.user
    if user.is_authenticated:

        data=VehicleDb.objects.get(id=cid)
        return render(request,"booknow.html",{'data':data})
    return redirect('login')


def savebooknow(request):
    if request.method == "POST":
        na = request.POST.get('carname')
        una=request.POST.get('username')
        bn = request.POST.get('brandname')
        pr = request.POST.get('price')
        vt = request.POST.get('vehicletype')
        put = request.POST.get('pickuptime')
        ph = request.POST.get('phonenumber')
        pot = request.POST.get('pickofftime')
        pu = request.POST.get('pickuplocation')
        do = request.POST.get('dropofflocation')
        pd = request.POST.get('pickupdate')
        dd = request.POST.get('dropoffdate')
        em=request.POST.get('email')
        obj = Bookingdb(carname=na,brandname=bn,price=pr,vehicletype=vt,pickuptime=put,pickofftime=pot,pickuplocation=pu,dropofflocation=do,pickupdate=pd,dropoffdate=dd,phonenumber=ph,username=una)
        obj.save()

        client_email=em
        ticket_details=na
        send_booking_confirmation_email(client_email,ticket_details)
        return redirect(carpage)

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page or another appropriate page after successful registration
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'login.html', {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            usr = authenticate(request, username=uname, password=pwd)
            if usr:
                login(request, user=usr)
                messages.success(request, 'login successfully')
                return redirect('index')
        messages.error(request, 'invalid credential')
        return render(request, 'login.html', {"form": form})
    
@login_required(login_url='login')
def log_out_view(request, *args, **kwargs):
    logout(request)
    messages.success(request, 'logout successfully')
    return redirect('index')



def userlogin(request):
    if request.method=="POST":
        un = request.POST.get('uname')
        pwd = request.POST.get('password')
        ml = request.POST.get('emaill')
        if signupdb.objects.filter(username=un,password=pwd,emailaddress=ml).exists():
            request.session['username'] = un
            request.session['password'] = pwd
            request.session['emailaddress'] = ml
            return redirect(index)
        else:
            return redirect(register)
    else:
        return redirect(register)
    




def userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(index)
# inside carpage navbar bookings

def bookingsdetail(request):
    data = Bookingdb.objects.filter(username=request.user.username)
    return render(request,"bookingsdetail.html",{'data':data})

#email verfication code
def send_booking_confirmation_email(client_email, ticket_details):
    subject = 'INDUS GO Booking Confirmation'
    message = f'Thanks for choosing INDUS GO your booking is confirmed.\n\n{ticket_details}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [client_email]

    try:
        send_mail(subject, message, email_from, recipient_list)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    except Exception as e:
        # Log the error or handle it as necessary
        return HttpResponse(f'Error sending email: {e}')

# def search_car(req):
#     if req.method=="POST":
#         search=req.POST.get("search")
#         search_item=search.upper()
#         s_cars=VehicleDb.objects.get(VehicleName=search_item)
#         return render(req,"search car.html",{'s_cars':s_cars})


