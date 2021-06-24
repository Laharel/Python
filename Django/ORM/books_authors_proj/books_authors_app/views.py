from django.shortcuts import redirect, render
from .models import Author, Book

# Create your views here.
def index(request):
    all_books = Book.objects.all()
    context = {
        "all_books": all_books,
    }
    return render(request, 'index.html', context)

def book_details(request, value):
    book_id = int(value)
    book = Book.objects.get(id=book_id)
    authors = Author.objects.all()
    context = {
        "book": book,
        "authors": authors,
    }
    return render(request, 'books.html', context)

def add_book(request):
    title_ = request.POST['title']
    desc_ = request.POST['desc']

    Book.objects.create(
        title = title_,
        desc = desc_,
    )

    return redirect('/')

def add_author_to_book(request):
    author_id = int(request.POST['authorr'])
    author = Author.objects.get(id=author_id)
    book_id = int(request.POST['book-id'])
    book = Book.objects.get(id=book_id)


    book.authors.add(author)

    return redirect('/books/'+str(book.id))

def authors(request):
    all_authors = Author.objects.all()
    context = {
        "all_authors": all_authors,
    }
    return render(request, 'authors.html', context)

def add_author(request):
    first_name_ = request.POST['first_name']
    last_name_ = request.POST['last_name']
    notes_ = request.POST['notes']

    Author.objects.create(
        first_name = first_name_,
        last_name = last_name_,
        notes = notes_
    )

    return redirect('/authors')

def author_details(request, value):
    author_id = int(value)
    author = Author.objects.get(id=author_id)
    books = Book.objects.all()
    context = {
        "author": author,
        "books": books,
    }
    return render(request, 'author_details.html', context)

def add_book_to_author(request):
    book_id = int(request.POST['book-id'])
    book = Book.objects.get(id=book_id)
    author_id = int(request.POST['author-id'])
    author = Author.objects.get(id=author_id)


    author.books.add(book)

    return redirect('/authors/'+str(author.id))