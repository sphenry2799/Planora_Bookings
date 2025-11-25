from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservations/edit/<int:pk>/', views.edit_reservation, name='edit_reservation'),
    path('reservations/delete/<int:pk>/', views.delete_reservation, name='delete_reservation'),
    path("profile/", views.profile_view, name="profile"),
]

