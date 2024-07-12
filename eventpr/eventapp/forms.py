from django import forms
from . models import Booking
class DateInput(forms.DateInput):
    input_type='date'



class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'


        widgets={
            'booking_date':DateInput
        }


        labels={
            'cus_name':"Customer Name:",
            'cus_phn':"Customer phone:",
            'Event name':"Event name:",
            'booking_date':"Booking Date:",
        }
        