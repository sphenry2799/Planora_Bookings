from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages  
from .forms import ReserveForm
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm 
from .models import Reservation 

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            from django.contrib import messages
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login') 
     
    else:
        form = UserRegistrationForm()

    return render(request, 'signup.html', {'form': form})

@login_required
def make_reservation(request):
    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()

            return redirect('reservation_confirmation')
    else:
        form = ReserveForm()

    return render(request, 'make_reservation.html', {'form': form})

# Reservation confirmation page
def reservation_confirmation(request):
    return render(request, "reservations/reservation_confirmation.html")

# Reservation list
def reservation_list(request):
    reservations = Reservation.objects.all().order_by('-date', '-time')
    return render(request, 'reservation_list.html', {'reservations': reservations})

# Edit reservation
def edit_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)

    if request.method == 'POST':
        form = ReserveForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, f"Reservation for {reservation.name} on {reservation.date} has been successfully updated.")
            return redirect('reservation_list')
    else:
        form = ReserveForm(instance=reservation, user=request.user)

    return render(request, 'edit_reservation.html', {'form': form})

# Delete reservation
def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)

    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')

    return render(request, 'delete_reservation.html', {'reservation': reservation})

# Profile view (optional)
def profile_view(request):
    return render(request, "profile.html")
