from django import forms
from .models import Booking, Contact,Review

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields ='__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model= Contact
        fields= '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model= Review
        fields= '__all__'