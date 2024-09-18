from django.shortcuts import render,redirect
from backend.models import categoryDb,VehicleDb
from carapp.models import Contactdb,Bookingdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.messages import success,error,warning
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required




# Create your views here.

def indexpage(request):
    return render(request,"index2.html")
def categorypage(request):
    return render(request,"addcategory.html")
def savecategory(request):
    if request.method == "POST":
        cn = request.POST.get('cname')
        img = request.FILES['image']
        obj = categoryDb(categoryname=cn,category_image=img)
        obj.save()
        success(request, "Added")
        return redirect(categorypage)
def displaycategory(request):
    data = categoryDb.objects.all()
    return render(request,"displaycategory.html",{'data':data})

def editcategory(request, editid):
    data = categoryDb.objects.get(id=editid)
    return render(request, "editcategory.html", {'data': data})

def updatecategory(request, updateid):
    if request.method == "POST":
        cn = request.POST.get('cname')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = categoryDb.objects.get(id=updateid).category_image

        categoryDb.objects.filter(id=updateid).update(categoryname=cn, category_image=file)
        return redirect(displaycategory)
def deletecategory(request, deleid):
    data = categoryDb.objects.filter(id=deleid)
    data.delete()
    success(request, "Deleted Successfully")
    return redirect(displaycategory)
def addvehicles(request):
    data=categoryDb.objects.all()
    return render(request,"addvehicles.html",{'data':data})
def savevehicle(req):
    if req.method == "POST":
        vn = req.POST.get('vname')
        bn = req.POST.get('bname')
        ec = req.POST.get('engcap')
        ml = req.POST.get('mile')
        fc = req.POST.get('fucap')
        mp = req.POST.get('mpower')
        vt = req.POST.get('vtype')
        pr = req.POST.get('price')
        img = req.FILES['image']
        obj = VehicleDb(VehicleName=vn, BrandName=bn, Enginecapacity=ec, Mileage=ml, Fuelcapacity=fc, Maxpower=mp, VehicleType=vt, VehiclePrice=pr, VehicleImage=img)
        obj.save()
        success(req,"Added")
        return redirect(addvehicles)

def displayvehicles(request):
    data = VehicleDb.objects.all()
    return render(request,"displayvehicles.html",{'data':data})
def editvehicle(request, editid):
    data = VehicleDb.objects.get(id=editid)
    return render(request, "editvehicles.html", {'data': data})
def updatevehicle(request, updateid):
    if request.method == "POST":
        vn = request.POST.get('vname')
        bn = request.POST.get('bname')
        vt = request.POST.get('vtype')
        vp = request.POST.get('price')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = VehicleDb.objects.get(id=updateid).VehicleImage

        VehicleDb.objects.filter(id=updateid).update(VehicleName=vn, BrandName=bn, VehicleType=vt, VehiclePrice=vp, VehicleImage=file)
        success(request, "Successfully updated")
        return redirect(displayvehicles)
def deletevehicle(request, deleid):
    data = VehicleDb.objects.filter(id=deleid)
    data.delete()
    success(request,"Deleted Successfully")

    return redirect(displayvehicles)

def messages(request):
    data = Contactdb.objects.all()
    return render(request,"messages.html",{'data':data})

# messages->seemessages->delete
def deletemesage(request,deleid):
    data = Contactdb.objects.filter(id=deleid)
    data.delete()
    success(request, "Deleted Successfully")
    return redirect(messages)

#Bookings -> displaycustomers
def displaycustomers(request):
    data = Bookingdb.objects.all()
    return render(request,"displaycustomers.html",{'data':data})
def deletecustomermessage(request,deleid):
    data = Bookingdb.objects.filter(id=deleid)
    data.delete()
    success(request, "Deleted Successfully")

    return redirect(displaycustomers)

def loginpage(request):
    return render(request,"loginpage.html")

def admin_login(req):
    if req.method=="POST":
        un = req.POST.get("username")
        pas = req.POST.get("pass")
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=pas)
            if x is not None:
                login(req,x)
                req.session['username']=un
                req.session['password']=pas
                return redirect(indexpage)
        else:
            return redirect(loginpage)
    else:
        return redirect(loginpage)
    
def admin_logout(req):
    del req.session['username']
    del req.session['password']
    return redirect(loginpage)
