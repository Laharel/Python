from django.shortcuts import render,redirect
import random
import datetime
# Create your views here.
def start(request):
    return redirect('/index')

def process_money(request):
    location = request.POST['gold']
    if location == "farm":
        earned = random.randint(10, 20)
        request.session['curr_gold'] += earned
        request.session['log'].append(f"Earned {earned} golds from {location}" +"  " + str(datetime.datetime.now()))
    elif location == "cave":
        earned = random.randint(5, 10)
        request.session['curr_gold'] += earned
        request.session['log'].append(f"Earned {earned} golds from {location}"+"  " + str(datetime.datetime.now()))
    elif location == "house":
        earned = random.randint(2, 5)
        request.session['curr_gold'] += earned
        request.session['log'].append(f"Earned {earned} golds from {location}"+"  " + str(datetime.datetime.now()))
    else :
        earned = random.randint(-50, 50)
        request.session['curr_gold'] += earned
        if earned >= 0 :
            request.session['log'].append(f"Earned {earned} golds from {location}"+"  " + str(datetime.datetime.now()))
        else:
            request.session['log'].append(f"Entered a casino and lost {-earned} golds...Ouch"+"  " + str(datetime.datetime.now()))


    return redirect('/index')

def index(request):
    if "curr_gold" not in request.session:
        request.session['curr_gold']=0
    if "log" not in request.session:
        request.session['log'] = []
    return render(request,"index.html")

def clear(request):
    request.session['curr_gold']=0
    request.session['log']=[]
    return redirect('/index')