from django.shortcuts import render
from django.http import HttpResponse
from . forms import *
from . models import *
def index(request):
    return render(request, "osat/index.html")


def about(request):
    return render(request, "osat/about.html")

def a_registration(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = detailsform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            a = alumni()
            a.fname = form['fname']
            a.lname = form['lname']
            a.lname = form['lname']
            a.save()
            return HttpResponse('Thank you for submitting'+str({{a.fname}}))
        else:
            return HttpResponse('Form invalid')

            # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, "osat/a_registration.html", {'detailsform': detailsform()})




