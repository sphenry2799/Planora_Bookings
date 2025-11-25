from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation
from .forms import ReserveForm

def home(request):
    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReserveForm()

    return render(request, 'reservation_home.html', {'form': form})

def edit_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)

    if request.method == 'POST':
        form = ReserveForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReserveForm(instance=reservation)

    return render(request, 'edit_reservation.html', {'form': form})

def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)

    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')

    return render(request, 'delete_reservation.html', {'reservation': reservation})

def reservation_list(request):
    reservations = Reservation.objects.all().order_by('-date', '-time')
    return render(request, 'reservation_list.html', {'reservations': reservations})

def profile_view(request):
    return render(request, "profile.html")

