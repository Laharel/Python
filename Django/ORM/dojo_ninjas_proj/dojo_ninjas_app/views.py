from django.shortcuts import render,redirect
from .models import Dojo,Ninja

# Create your views here.

def index(request):

    all_dojos = Dojo.objects.all()

    context = {
        "all_dojos": all_dojos,
    }
    return render(request, 'index.html', context)

def add_dojo(request):
    
    dojo_name = request.POST['name']
    dojo_city = request.POST['city']
    dojo_state = request.POST['state']
    
    new_dojo = Dojo.objects.create(
        name=dojo_name,
        city=dojo_city,
        state=dojo_state
    )
    return redirect('/')

def add_ninja(request):
    fname = request.POST['first_name']
    lname = request.POST['last_name']
    dojo_id = int(request.POST['dojo'])
    dojo = Dojo.objects.get(id=dojo_id)
    new_ninja=Ninja.objects.create(
        first_name = fname,
        last_name=lname,
        dojo=dojo      
    )        
    
    return redirect('/')


def delete_dojo(request):

    dojo_id = int(request.POST['dojo'])
    dojo = Dojo.objects.get(id=dojo_id).delete()

    return redirect('/')