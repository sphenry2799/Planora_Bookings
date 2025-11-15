from django.shortcuts import render
from django.http import HttpResponse
from .models import Reservation
from .forms import ReserveForm

# Home page view
def home(request):
    return HttpResponse("Welcome to Planora Reservations!")

# List all reservations
def reservation_list(request):
    reservations = Reservation.objects.all()  # fetch all reservations
    return render(request, 'reservations/list.html', {'reservations': reservations})

def ReserveForm(request):

    context = {}

    return render(request , 'reservations/resevation.html' , context)