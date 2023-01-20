from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from django.core import serializers
from datetime import timedelta


@login_required(login_url='login')
def create_graphic(request):
    doctors = Doctor.objects.all()
    staffs = Staff.objects.all()
    neighborhoods = Neighborhood.objects.all()
    streets = Street.objects.all()
    addresses = Address.objects.all()
    context = {
        'staffs': staffs,
        'neighborhoods': neighborhoods,
        'streets': streets,
        'addresses': addresses,
        'doctors': doctors,
        }
    return render(request, 'create_graphic.html', context)


@login_required
def table_page(request):
    user = request.user
    user_id = request.user.id
    works_day = Work.objects.filter(doctor__user=user)
    if not works_day.exists():
        works_day = Work.objects.filter(staff=user_id)
    # print(works_day)
    context = {'works_day': works_day}
    
    for i in works_day:
        d = i.date
        print(d + timedelta.days(7))
    return render(request, 'table.html', context)


def get_streets(reuqest):
    item = reuqest.GET.get("item").strip()
    streets = Street.objects.filter(neighborhood__name=item)
    data = serializers.serialize('json', streets)
    return HttpResponse(data, content_type="application/json")


def get_address(reuqest):
    item = reuqest.GET.get("item").strip()
    address = Address.objects.filter(street__name=item)
    data = serializers.serialize('json', address)
    return HttpResponse(data, content_type="application/json")


def save_grafic(request):
    doctor = request.GET.get("doctor")
    neighborhood = request.GET.get("neighborhood")
    street = request.GET.get("street")
    doctor = Doctor.objects.get(full_name=doctor)
    neighborhood = Neighborhood.objects.get(name=neighborhood)
    street = Street.objects.filter(neighborhood=neighborhood)
    staffs = Staff.objects.filter(doctor__full_name=doctor)
    work = Work(
        doctor=doctor,
        neighborhood=neighborhood,
    )
    work.save()
    for i in staffs.values():
        work.staff.add(i['id'])
    for i in street.values():
        work.street.add(i['id'])
    return HttpResponse('True')


def login_page(request):
    context = {}
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        usr = authenticate(username=uname, password=pwd)
        if usr:
            login(request, usr)
            return redirect('create_graphic')
        else:
            context['message'] = 'username yoki parol xato!!!'
            context['col'] = 'danger'
    return render(request, 'login.html', context)


@login_required
def logout_page(request):
    logout(request)
    return redirect('create_graphic')