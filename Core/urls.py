from django.urls import path
from .views import *

urlpatterns = [
    path("staff/view/", viewStaff, name="view_staff"),
    path("staff/edit/<str:pk>", editstaff, name="edit_staff"),
    path("staff/delete/<str:pk>", deletestaff, name="delete_staff")
]