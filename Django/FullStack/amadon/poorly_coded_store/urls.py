from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('checkout', views.display_checkout),
    path('checkout/', views.checkout)
]
