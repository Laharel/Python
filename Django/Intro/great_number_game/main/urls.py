from django.urls import path
from . import views

urlpatterns = [
    path('',views.start),
    path('index',views.index),
    path('guess',views.guess),
    path('clear',views.clear)
]