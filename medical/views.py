from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from django.core import serializers
from .utils import get_now_month


@login_required(login_url='login')
def create_graphic(request):
    staffs = Staff.objects.all()
    neighborhoods = Neighborhood.objects.all()
    streets = Street.objects.all()
    addresses = Address.objects.all()
    context = {
        'staffs': staffs,
        'neighborhoods': neighborhoods,
        'streets': streets,
        'addresses': addresses,
        }
    return render(request, 'create_graphic.html', context)


@login_required
def table_page(request):
    return render(request, 'table.html')


def get_user_table_works(request):
    user = request.GET.get('req')
    works_day = Work.objects.filter(staff__user__username=user)
    data = serializers.serialize('json', works_day)
    return HttpResponse(data, content_type="application/json")


def get_streets(reuqest):
    item = reuqest.GET.get("item").strip()
    streets = Street.objects.filter(neighborhood__name=item)
    data = serializers.serialize('json', streets)
    return HttpResponse(data, content_type="application/json")


def get_address(reuqest):
    item = reuqest.GET.getlist("item[]")
    address = Address.objects.filter(street__slug__in=item)
    print(address)
    data = serializers.serialize('json', address)
    return HttpResponse(data, content_type="application/json")


def save_grafic(request):
    staff = request.GET.get("staff")
    date = request.GET.get("date")
    address = request.GET.getlist("addresses[]")
    staff = Staff.objects.get(full_name=staff)
    for addr in address:
        address = Address.objects.get(pk=int(addr))
        Work.objects.create(
            staff=staff,
            address=address,
            date=date
        )
    return HttpResponse('True')


def adresses_work(request):
    works = Work.objects.filter(staff__user=request.user)
    context = {'addresses': works}
    return render(request, 'adresses_work.html', context)


def jadval(request):
    staffs = Staff.objects.all()
    works = []
    for s in staffs:
        w = Work.objects.filter(staff__user=s.user)
        if w.exists():
            works.append(w)
    print(works)
    # works = Work.objects.all()
    context = {'works': works}
    return render(request, 'jadval.html', context)


def login_page(request):
    context = {}
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        usr = authenticate(username=uname, password=pwd)
        if usr:
            login(request, usr)
            return redirect('table')
        else:
            context['message'] = 'username yoki parol xato!!!'
            context['col'] = 'danger'
    return render(request, 'login.html', context)


@login_required
def logout_page(request):
    logout(request)
    return redirect('create_graphic')