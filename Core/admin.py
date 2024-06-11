from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("regno", "fname", "mname", "position")