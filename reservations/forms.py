from django import forms
from .models import Reservation

class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        widgets = {
    'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
    'name': forms.TextInput(attrs={'class': 'form-control'}),
    'guests': forms.NumberInput(attrs={'class': 'form-control'}),  # FIXED
    'notes': forms.Textarea(attrs={'class': 'form-control'}),
}

