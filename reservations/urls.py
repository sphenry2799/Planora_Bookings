from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home / reservation form
    path("reservation_confirmation/", views.reservation_confirmation, name="reservation_confirmation"),
    path('list/', views.reservation_list, name='reservation_list'),
    path('edit/<int:pk>/', views.edit_reservation, name='edit_reservation'),
    path('delete/<int:pk>/', views.delete_reservation, name='delete_reservation'),
]

