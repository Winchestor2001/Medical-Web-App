from django.urls import path
from . import views



urlpatterns = [
    path('', views.create_graphic, name='create_graphic'),
    path('table/', views.table_page, name='table'),
    path('get_streets/', views.get_streets, name='get_streets'),
    path('get_address/', views.get_address, name='get_address'),
    path('save_grafic/', views.save_grafic, name='save_grafic'),

    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
]