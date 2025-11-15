from django import forms
from .models import reservation

class ReserveForm(forms.Modelform):
   class Meta:
      model = reservation
      fields = '__all__'