from django.contrib import admin
from django.urls import path
from .views import visitors_page, make_booking,contact, review, show_bookings, staff_interface, show_booking_by_id

urlpatterns = [
    path('',visitors_page,name='visitors_homepage'),
    path('make_booking', make_booking, name="make_booking"),
    path('contact_us', contact, name='contact'),
    path('review', review, name='review'),
    path('staff_interface',staff_interface,name="staff_interface"),
    path('show_bookings', show_bookings, name="show_bookings"),
    path('booking_by_id/<int:id>',show_booking_by_id,name="booking_by_id")

]