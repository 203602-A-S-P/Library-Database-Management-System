from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'home/index.html')

def home(request):
    return render(request,'home/section.html')


def dashboard(request):
    return render(request,'home/dashboard.html')

def search(request):
    return render(request,'home/search.html')

def history(request):
    return render(request,'home/history.html')

def notification(request):
    return render(request,'home/notification.html')

def account(request):
    return render(request,'home/account.html')
