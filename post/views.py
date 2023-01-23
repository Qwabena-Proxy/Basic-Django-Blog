from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Post

# Create your views here.
def index(request):
    blogData= Post.objects.all()
    list= [0,1,2,3,4,5]
    return render(request, 'index.html', {'post':blogData})

def cotentpage(request, title):
    selected= title
    data= Post.objects.all()
    for i in data:
        if i.Title == title:
            blogtitle= i.Title
            blogdate= i.DateTime
            blogdescription= i.Description
    contex= {
        'title': blogtitle,
        'dateandtime': blogdate,
        'content': blogdescription,
    }
    return render(request, 'content.html', contex)

def login(request):
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
