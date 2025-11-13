from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # main page
    path('reservations/', views.reservation_list, name='reservation_list'),
]
