from django.urls import path
from . import views
urlpatterns = [
    path('',views.toshows),
    path('shows',views.shows),
    path('add',views.add,name="add_show"),
    path('shows/<int:id>',views.show,name="this_show"),
    path('shows/<int:id>/edit',views.edit,name="edit_show"),
    path('shows/<int:id>/update',views.update,name="edit_show"),
    path('shows/<int:id>/destroy',views.delete,name="delete_show"),
]
