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


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['addres_name', 'full_name', 'street']


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['staff', 'address', 'checked', 'date']


@admin.register(SmsCode)
class SmsCodeAdmin(admin.ModelAdmin):
    list_display = ['number', 'code', 'date']



