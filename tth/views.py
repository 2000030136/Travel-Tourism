from django.shortcuts import render

# Create your views here.
def basic(request):
    return render(request,'basic.html')
def index(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')
def tours(request):
    return render(request,'tours.html')
def contact(request):
    return render(request,'contact.html')
def cards(request):
    return render(request,'cards.html')
def payment(request):
    return render(request,'payment.html')
def australia(request):
    return render(request,'australia.html')
