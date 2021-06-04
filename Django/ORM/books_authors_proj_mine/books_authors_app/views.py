from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        "allbooks" : Book.objects.all()
    }
    return render(request,'index.html',context)

def addbook(request):
    Book.objects.create(title=request.POST['title'])
    return redirect('')

def book(request,number):
    context={
        "book":Book.objects.get(id=number)
    }
    return render(request,"book.html",context)

def authors(request):
    context={
        "allauthors" :Author.objects.all()
    }
    return render(request,"authors.html",context)

def addauthor(request):
    Author.objects.create(first_name=request.POST['fname'],
    last_name=request.POST['lname'])
    return redirect('')

def author(request,number):
    context={
        "author":Author.objects.get(id=number)
    }
    return render(request,"author.html",context)