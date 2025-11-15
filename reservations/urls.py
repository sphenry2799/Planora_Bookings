from django.contrib import admin
from django.urls import path
from reservations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # home page → reservation form
]
