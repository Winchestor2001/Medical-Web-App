from django.contrib import admin
from .models import *


@admin.register(Neighborhood)
class NeighborhoodAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'population']


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'population']


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'rank']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['full_name']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['addres_name', 'full_name', 'street']


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'neighborhood', 'date']




