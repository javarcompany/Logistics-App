from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', loginuser, name = 'login'),
    path('logout', logoutuser, name="logout"),
    path('change_psw', change_psw, name="change_psw")

]