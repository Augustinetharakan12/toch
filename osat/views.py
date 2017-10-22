import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from . forms import *
from . models import *
def index(request):
    dn=datetime.datetime.now()
    cont_dict={'notif' : notif.objects.all().order_by('-timestamp')[:2],'dn':dn}
    return render(request, "osat/index.html", cont_dict)


def about(request):
    return render(request, "osat/about.html")

def a_registration(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = detailsform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            a=form.save(commit=False)
            form.save()
            #print ("hello")
            #print (a.fname)
            return render(request,'osat/submit.html', {'a':a})
        else:
            return HttpResponse('Form invalid')

            # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, "osat/a_registration.html", {'detailsform': detailsform()})
def h_registration(request):
    return render(request,"osat/h_registration.html")
def e_registration(request):
    return render(request,"osat/e_registration.html")
def c_us(request):
    return render(request,"osat/c_us.html")

def h_registration(request):
    return render(request,"osat/h_registration.html")
def e_registration(request):
    return render(request,"osat/e_registration.html")
def c_us(request):
    return render(request,"osat/c_us.html")



def notific(request):
    dn = datetime.datetime.now()
    cont_dict2 = {'notif': notif.objects.all().order_by('-timestamp'), 'dn': dn}
    return render(request, "osat/notifications.html", cont_dict2)



def example(request):
    return JsonResponse({"data": "hello world"})




def ec_registration(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ec_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            a=form.save(commit=False)
            form.save()
            print ("hello")

            return render(request,'osat/submit.html', {'a':a})
        else:
            return HttpResponse('Form invalid')

            # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, "osat/ec_registration.html", {'ec_form': ec_form()})


def er_registration(request):
    a=ec
    a=a.objects.all()
    return render(request,"osat/er_registration.html",{'a':a})

def el_registration(request):
    return render(request,"osat/el_registration.html")


