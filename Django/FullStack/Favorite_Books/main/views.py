from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User,Book
import bcrypt
# Create your views here.
def index(request):
    return render(request,'index.html')

def reg(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['pwd']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        this=User.objects.create(
            first_name=request.POST['fn'],
            last_name=request.POST['ln'],
            email=request.POST['email'],
            password=pw_hash,
            )
        request.session['uid']=this.id
        return redirect('/books')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if errors:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect("/")
    else:
        this = User.objects.get(email = request.POST['email'])
        request.session['uid'] = this.id
        return redirect("/books")

def books(request):
    if 'uid' in request.session:
        this = User.objects.get(id=request.session['uid'])
        books = Book.objects.all()
        mybooks = this.books.all()
        context={
            'this' : this,
            'books' : books,
            'mybooks' : mybooks
        }
        return render(request,'books.html',context)
    else:
        return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')


def add(request):
    if 'uid' in request.session:
        errors = Book.objects.book_valiadtor(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.errors(request, value)
            return redirect('/books/new')
        else:
            this = User.objects.get(id=request.session['uid'])    
            book=Book.objects.create(
            title = request.POST['title'],
            description = request.POST['desc'],
            uploaded_by = this
            )
            this.liked_books.add(book)
            return redirect('/books')
    else:
        return redirect('/')

def delete(request,id):
    if 'uid' in request.session:
        this = User.objects.get(id=request.session['uid'])
        this.books.get(id=id).delete()
        return redirect("/books")
    else:
        return redirect('/')

def remove(request,id):
    if 'uid' in request.session:
        this = User.objects.get(id=request.session['uid'])
        book = Book.objects.get(id=id)
        this.liked_books.remove(book)
        return redirect("/books")
    else:
        return redirect('/')

def edit(request,id):
    if 'uid' in request.session:
        this = User.objects.get(id=request.session['uid'])
        book = this.books.get(id=id)
        context={
            'this':this,
            'book':book,
        }
        return render(request, 'edit.html', context)
    else:
        return redirect('/')

def book(request,id):
    if 'uid' in request.session:
        this = User.objects.get(id=request.session['uid'])
        book = Book.objects.get(id=id)
        context={
            'this':this,
            'book':book,
        }
        return render(request, 'book.html', context)
    else:
        return redirect('/')

def update(request, id):
    if 'uid' in request.session:
        errors = Book.objects.book_valiadtor(request.POST)
        book = Book.objects.get(id=id)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/books/edit/'+str(id))
        else:
            book.title = request.POST['title']
            book.description = request.POST['desc']
            book.save()
            return redirect('/books')
    else:
        return redirect('/')

def like(request,id):
    if 'uid' in request.session:
        this = User.objects.get(id = request.session['uid'])
        book = Book.objects.get(id = id)
        this.liked_books.add(book)
        return redirect('/books')
    else:
        return redirect('/')
