from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
from .forms import ReserveForm

User = get_user_model()

class TestReserveForm(TestCase):

    def test_reservation_form_is_valid(self):
        # Create a user for the reservation
        user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )

        reservation_date = (timezone.now() + timedelta(days=1)).date()

        form = ReserveForm({
            'user': user.id,
            'name': 'John Doe',
            'date': reservation_date,
            'time': '18:30',
            'guests': 2,
            'notes': 'Window seat'
        })

        print(form.errors)  # temporary debug
        self.assertTrue(form.is_valid())
