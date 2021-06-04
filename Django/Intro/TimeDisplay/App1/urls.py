from django.urls import path
from . import views

urlpatterns = [
    path('',views.one),
    path('time_display',views.one),
]
