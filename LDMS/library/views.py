from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import BookForm


# Create your views here.

# def index(request):
#     form = CreateUserForm()
#     context = {'form':form}
#     if request.method == 'POST':  
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             email = form.cleaned_data.get('email')

#             print(user,email)
#             return redirect('home')
#         else:
#             print("epty")
            
#             # context.update({"value":"fail"})
#             # return render(request,"designer/register.html",context)
#             #check whether its printing in console
             
#             #messages.info(request,'Failed')
       
    
#     print(context)
    
#     return render(request,'home/main.html',context)

def home(request):
    # form = CreateUserForm()
    # context = {'form':form}
    if request.method == 'POST':  
        # form = CreateUserForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)

        user1 = authenticate(request, username = username , password = password)
        print("Not a user")
        if user1 is not None:
            login(request,user1)

            return redirect('dashboard')
        else:
            print("fail")
        
    return render(request,'home/section.html')

def book(request):
    return render(request,'home/singlebook.html')

def dashboard(request):
    return render(request,'home/dashboard.html')

def search(request):
    books = Book.objects.all()
    context ={'books':books}
    return render(request,'home/search.html',context)

def addbook(request):
 
    form=BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('search')
        else:
            print('invalid da.......')
            return redirect('addbook')
#   print('brand:'+ str(bname))
    context ={'form':form}   
    

    return render(request,'home/addbook.html',context)

def history(request):
    return render(request,'home/history.html')

def notification(request):
    return render(request,'home/notification.html')

def account(request):
    return render(request,'home/account.html')
