from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows/new', views.new_show_form),
    path('shows/create', views.create_show),
    path('shows/<int:id>', views.show_details, name='show-details'),
    path('shows', views.shows),
    path('shows/<int:id>/edit', views.edit_show, name='show-edit'),
    path('shows/<int:id>/update', views.update_show, name='show-update'),
    path('shows/<int:id>/destroy', views.destroy_show, name='show-destroy'),
]