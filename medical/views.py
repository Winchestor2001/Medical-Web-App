from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from django.core import serializers
from random import randint
from .utils import send_verify_code
from datetime import datetime
from .utils import get_works_jadval
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile


@login_required(login_url='login')
def create_graphic(request):
    staffs = Staff.objects.all().order_by('full_name')
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
    print(request.GET)
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


@login_required
def adresses_work(request, date):
    date = datetime.strptime(date, "%Y-%m-%d")
    print(date)
    works = Work.objects.filter(staff__user=request.user, date=date)
    context = {'addresses': works}
    return render(request, 'adresses_work.html', context)


@login_required
def jadval(request):
    staffs = Staff.objects.all()
    if request.user.username == 'root':
        works = get_works_jadval(staffs)
    else:
        works = []
        w = Work.objects.filter(staff__user=request.user)
        if w.exists():
            checked_count = 0
            addresses = []
            for ch in w:
                if ch.checked:
                    checked_count += 1
                    addresses.append(ch.address.addres_name)
            works.append((w, checked_count, addresses))
    
    context = {'works': works}
    return render(request, 'jadval.html', context)


def send_sms(request):
    code = randint(1000, 9999)
    user_number = request.GET['number']
    try:
        user = SmsCode.objects.get(number=user_number)
        user.code = code
        user.save()
    except:
        SmsCode.objects.create(
            number=request.GET['number'],
            code=code
        )
    # data = serializers.serialize('json', address)
    # return HttpResponse(data, content_type="application/json")
    # send_verify_code(code, user_number)
    return HttpResponse(code)


@csrf_exempt
def correct_sms_code(request):
    number = request.POST['code']
    user = request.POST['user']
    date = request.POST['date']
    img = request.POST['img']
    image = ContentFile(img, f'{user}.jpg')
    date = datetime.strptime(date, '%Y-%m-%d')
    work = Work.objects.filter(address__phone_number=number, staff__user__username=user, date=date)
    work = work[0]
    work.checked = True
    work.img = image
    work.save()
    SmsCode.objects.get(number=number).delete()
    return HttpResponse(True)


def get_staff_imgs(request):
    imgs = Work.objects.filter(staff__full_name=request.GET['staff'])
    data = serializers.serialize('json', imgs)
    return HttpResponse(data, content_type="application/json")


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