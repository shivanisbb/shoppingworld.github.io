from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader

from shop.forms import personad,regad,loginad
from django.contrib.auth import authenticate,login
from django.contrib import messages
from math import ceil
import json

def home(request):
    return render(request,"shop/home.html")



def contact(request):
    if request.method=='POST':
        per=personad(request.POST)
        per.save()
        if per.is_valid():
            try:
                return redirect('/')
            except:
                pass
    else:
           per=personad()

    return render(request,"shop/contact.html",{'form':per})

def registrationpage(request):
    if request.method=='POST':
       form=regad(request.POST)
       print('signed in')
       if form.is_valid():
           form.save()
           messages.success(request, 'account successfully created')
           print(form.cleaned_data)
           try:
              return redirect('register')
           except:
               pass
    else:
           form=regad()
    return render(request,"shop/registrationpage.html",{"form":form})

def loginpage(request):
      log= loginad(request.POST or None)

      if log.is_valid():
        print(log.cleaned_data)
        username = log.cleaned_data.get('username')
        password = log.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
           login(request, user)
           return redirect('/login')
        else:
            pass
        print("error")
      else:
          log=loginad()

      return render(request, "shop/loginpage.html", {'form':log})


