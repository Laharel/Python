from django.urls import path
from .import views

urlpatterns = [
    path('',views.index),
    path('addbook',views.addbook),
    path('book/<int:number>',views.book),
    path('authors',views.authors),
    path('addauthor',views.addauthor),
    path('author/<int:number>',views.author),
]