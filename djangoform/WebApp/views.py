from django.shortcuts import render
from WebApp.forms import NewUser


# Create your views here.
def index(request):
    return render(request,'WebApp/index.html')

def page(request):
    return render(request,'WebApp/page.html')

def other(request):
    return render(request,'WebApp/other.html')


def users(request):
    form=NewUser()
    if request.method=='POST':
        form=NewUser(request.post)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else :
            print("Error")
    return render(request,"WebApp/form_page.html",{'form':form})
