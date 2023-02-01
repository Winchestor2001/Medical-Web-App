from django.urls import path
from . import views



urlpatterns = [
    path('', views.table_page, name='table'),
    path('create_graphic/', views.create_graphic, name='create_graphic'),
    path('get_user_table_works/', views.get_user_table_works, name='get_user_table_works'),
    path('get_streets/', views.get_streets, name='get_streets'),
    path('get_address/', views.get_address, name='get_address'),
    path('save_grafic/', views.save_grafic, name='save_grafic'),
    path('jadval/', views.jadval, name='jadval'),
    path('adresses_work/<str:date>', views.adresses_work, name='adresses_work'),
    path('send_sms/', views.send_sms, name='send_sms'),
    path('correct_sms_code/', views.correct_sms_code, name='correct_sms_code'),
    path('get_staff_imgs/', views.get_staff_imgs, name='get_staff_imgs'),

    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
]