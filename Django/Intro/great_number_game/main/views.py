from django.shortcuts import render,redirect
import random
# Create your views here.
def start(request):
    request.session['number']=int(random.randint(1, 100))
    request.session['counter'] = int(0)
    print("number",request.session['number'])
    return redirect('/index')

def index(request):
    return render(request,"index.html")

def guess(request):
    request.session['counter'] += int(1)
    request.session['guess']=int(request.POST['guess'])
    print("guess",request.session['guess'])
    return redirect('/index')

def clear(request):
    del request.session['counter']
    del request.session['guess']
    return redirect('/')