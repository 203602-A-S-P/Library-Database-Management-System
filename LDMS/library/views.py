from django.shortcuts import render,redirect
from .forms import CreateUserForm

# Create your views here.

def index(request):
    form = CreateUserForm()
    context = {'form':form}
    if request.method == 'POST':  
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            print(user,email)
            return redirect('home')
        else:
            print("epty")
            
            # context.update({"value":"fail"})
            # return render(request,"designer/register.html",context)
            #check whether its printing in console
             
            #messages.info(request,'Failed')
       
    
    print(context)
    
    return render(request,'home/index.html',context)

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
