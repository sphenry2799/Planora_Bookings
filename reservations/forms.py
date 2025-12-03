from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Reservation 
from django.core.exceptions import ValidationError 
from datetime import date 



class ReserveForm(forms.ModelForm):
    guests = forms.IntegerField(
        min_value=1, 
        max_value=12,  
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None) 
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        time = cleaned_data.get("time")

            # Only run if date, time, and user are available
        if date and time and self.user:
            query = Reservation.objects.filter(
                date=date, 
                time=time, 
                user=self.user
            )

            if self.instance and self.instance.pk:
                query = query.exclude(pk=self.instance.pk)

            if query.exists():
                raise ValidationError(
                    "You already have a reservation booked for this exact date and time."
                )
            
        return cleaned_data
        
    class Meta:
        model = Reservation
        fields = ['date', 'time', 'name', 'guests', 'notes']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'guests': forms.NumberInput(attrs={'class': 'form-control'}), 
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }

class UserRegistrationForm(UserCreationForm):
    pass

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields 
 
def clean_date(self):
        reservation_date = self.cleaned_data['date']
        if reservation_date < date.today():
            raise ValidationError("You cannot book a reservation for a past date.")
        return reservation_date

      