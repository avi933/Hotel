from django import forms
from .models import Booking, Contact,Review

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields ='__all__'
        widgets = {
            'checkin_date': forms.DateInput(attrs={'class': 'datepicker', 'placeholder':'xxxx-tx-xx', 'type':'date', 'id': 'checkin_date'}),
            'checkout_date': forms.DateInput(attrs={'class': 'datepicker', 'placeholder':'xxxx-tx-xx', 'type':'date', 'id': 'checkout_date'})
        }
        exclude = ['booking_date',]

class ContactForm(forms.ModelForm):
    class Meta:
        model= Contact
        fields= '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model= Review
        fields= '__all__'