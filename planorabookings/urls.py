from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', RedirectView.as_view(pattern_name='account_login', permanent=False), name='home'),
    path('reservations/', include('reservations.urls')),
    path('summernote/', include('django_summernote.urls')),
   
 ]