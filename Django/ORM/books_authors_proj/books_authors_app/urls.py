from django.conf.urls import url
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index),
    path('books/<int:value>', views.book_details, name='books'),
    path('add_book', views.add_book),
    path('add_author_to_book', views.add_author_to_book),

    path('authors', views.authors),
    path('authors/<int:value>', views.author_details, name='authors'),
    path('add_author', views.add_author),
    path('add_book_to_author', views.add_book_to_author),


]