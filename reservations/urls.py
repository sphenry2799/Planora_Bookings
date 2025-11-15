from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # home page → reservation form
    path('reservations/', views.reservation_list, name='reservation_list'),
]
