from django.shortcuts import render,redirect
from .models import User

# Create your views here.
def index(request):
    context = {
    	"all_the_users": User.objects.all()
    }
    return render(request,'index.html',context)

def create_user(request):
    request.session['first_name'] = request.POST['first_name']
    first = request.session['first_name']
    request.session['last_name'] = request.POST['last_name']
    last = request.session['last_name']
    request.session['email'] = request.POST['email']
    email = request.session['email']
    request.session['age'] = request.POST['age']
    age = int(request.session['age'])
    User.objects.create(first_name =f"{first}",last_name = f"{last}",Email = f"{email}", Age=age )
    return redirect('/')