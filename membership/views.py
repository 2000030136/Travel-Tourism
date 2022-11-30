from django.shortcuts import render, redirect
from numpy import random

from .models import MemberData
from .forms import MembershipForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
# Create your views here.
# def memberdetails(request):
#     return render(request,'membership/memberdetails.html',{'title':'MemberDetails'})

# def viewmemberdetails(request):
#     return render(request,'membership/viewmemberdetails.html',{'title':'View','members':MemberData.objects.all()}) #select statement
def piechart(request):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:

    import numpy as np

    # Creating dataset
    cars = ['AUDI', 'BMW', 'FORD',
            'TESLA', 'JAGUAR', 'MERCEDES']

    data = [23, 17, 35, 29, 12, 41]

    # Creating plot
    fig = plt.figure(figsize=(10, 7))
    plt.pie(data, labels=cars)

    # show plot
    plt.show()
    return render(request,'piechart.html')

def addmember(request):
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            form.save() #inserting data into table
            return redirect('../basic')
    else:
        form = MembershipForm()
    return render(request,'membership/addmember.html',{'title':'New Member','form':form})
def name(request):
    return render(request,"membership/login.html")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() #inserting data into table
            username=form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            login(request, user)
            return redirect('../accounts/login')
    else:
        form = UserCreationForm()
    context={'form':form}
    return render(request,'registration/register.html',context)

