from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("reservation_confirmation/", views.reservation_confirmation, name="reservation_confirmation"),
    path('list/', views.reservation_list, name='reservation_list'),
    path('edit/<int:pk>/', views.edit_reservation, name='edit_reservation'),
    path('delete/<int:pk>/', views.delete_reservation, name='delete_reservation'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('reserve/', views.make_reservation, name='make_reservation'),
]