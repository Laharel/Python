from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User
import bcrypt
# Create your views here.
def index(request):
    return render(request,'index.html')

def new(request):
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = User.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['pwd']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        this=User.objects.create(
            first_name=request.POST['fname'],
            last_name=request.POST['lname'],
            email=request.POST['email'],
            password=pw_hash,
            date_of_birth=request.POST['dob']
            )
        request.session['userid']=this.id
        return redirect('/success')

def login(request):
    email = User.objects.filter(email=request.POST['email'])
    if email:
        logged_user = email[0] 
        if bcrypt.checkpw(request.POST['pwd'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/success')
    return redirect('/')

def success(request):
    if 'userid' in request.session:
        context={
            'email':User.objects.get(id=request.session['userid']),
        }
        return render(request,'success.html',context)
    else:
        return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')