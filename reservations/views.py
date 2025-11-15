from django.shortcuts import render, redirect
from .forms import ReserveForm

def home(request):
    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # you could redirect to a success page
    else:
        form = ReserveForm()
    
    return render(request, 'reservation_home.html', {'form': form})

