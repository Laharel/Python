from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('login',views.login),
    path('wall',views.wall),
    path('logout',views.logout),
    path('message',views.message),
    path('comment/<int:id>',views.comment),
    path('delete/<int:id>',views.delete),
]
