from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

# Create your views here.
@login_required(login_url = 'login')
def viewStaff(request):
    staff_objects = Staff.objects.all()

    context = {"Staffs":staff_objects}
    return render(request, "core/staff/viewstaff.html", context)

@login_required(login_url='login')
def editstaff(request, pk):
    staff_object = Staff.objects.get(id = pk)
    context = {"Staff":staff_object}
    return render(request, "core/staff/editstaff.html", context)

@login_required(login_url='login')
def deletestaff(request, pk):
    staff_object = Staff.objects.get(id = pk)
    context = {"Staff":staff_object}
    messages.error(request, "You arr about to delete a record")
    messages.warning(request, "You are about....")
    messages.info(request, "You are doing wjat....?")
    messages.success(request, "Am hereeeee.....")
    return render(request, "core/staff/deletestaff.html", context)