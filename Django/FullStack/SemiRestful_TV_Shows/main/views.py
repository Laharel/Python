from django.shortcuts import render,redirect
from .models import Show

# Create your views here.
def toshows(request):
    return redirect('/shows')

def shows(request):
    context = {
        'allshows':Show.objects.all()
    }
    return render(request,'shows.html',context)

def add(request):
    Show.objects.create(
        title=request.POST['title'],
        network=request.POST['netwrok'],
        release_date=request.POST['date'],
        desc=request.POST['desc']
    )
    return render(request,'add.html')

def show(request,id):
    context = {Show.object.get(id=id)}
    return render(request,'show.html',context)

def edit(request,id):
    context = {Show.object.get(id=id)}
    return render(request,'edit.html',context)

def update(request,id):
    Show.object.get(id=id).title=request.POST['title']
    Show.object.get(id=id).network=request.POST['network']
    Show.object.get(id=id).release_date=request.POST['date']
    Show.object.get(id=id).desc=request.POST['desc']
    Show.object.get(id=id).save()
    return redirect('/shows/<int:id>')

def delete(request,id):
    Show.objects.get(id=id).delete()
    return redirect('/shows')