from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('reg',views.reg),
    path('login',views.login),
    path('logout',views.logout),
    path('books',views.books),
    path('books/<int:id>/delete',views.delete),
    path('books/<int:id>/remove',views.remove),
    path('books/add',views.add),
    path('books/<int:id>/edit',views.edit),
    path('books/<int:id>/update',views.update),
    path('books/<int:id>/',views.book),
    path('books/<int:id>/like',views.like),
]