from django.shortcuts import render
from .forms import AboutForm

def about(request):
    if request.method == 'POST':
        form = AboutForm(request.POST)
        if form.is_valid():
            # Handle form: save or send email
            return render(request, 'about.html', {'form': AboutForm(), 'success': True})
    else:
        form = AboutForm()
    
    return render(request, 'about/about.html', {'form': form})

