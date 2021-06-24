from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import bcrypt
# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
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
        fn=request.POST['fn'],
        ln=request.POST['ln'],
        email=request.POST['email'],
        pwd=pw_hash,
            )
    request.session['this']=this.id
    return redirect('/wall')

def login(request):
    email = User.objects.filter(email=request.POST['email'])
    if email:
        this = email[0] 
        if bcrypt.checkpw(request.POST['pwd'].encode(), this.pwd.encode()):
            request.session['this'] = this.id
            return redirect('/wall')
    return redirect('/')

def wall(request):
    if 'this' in request.session:
        this = User.objects.get(id=request.session['this'])
        context={
            'this':this,
            'messages':Message.objects.all(),
            'comments':Comment.objects.all(),
            'mycomments':this.comments.all()
        }
        return render(request,'wall.html',context)
    else:
        return redirect('/')

def message(request):
    errors = Message.objects.message_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        Message.objects.create(
            message = request.POST['msg'],
            user = User.objects.get(id=request.session['this'])
        )
        return redirect('/wall')

def comment(request, id):
    errors = Comment.objects.comment_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        Comment.objects.create(
            comment = request.POST['cmt'],
            user = User.objects.get(id=request.session['this']),
            post = Message.objects.get(id=id)
        )
        return redirect('/wall')

def delete(request,id):
    this=User.objects.get(id=request.session['this'])
    this.comments.get(id=id).delete()
    return redirect('/wall')

def logout(request):
    request.session.flush()
    return redirect('/')