from ast import BoolOp
from django.shortcuts import render, redirect
from .models import Vacancies,Booking,Contact,Review
from .forms import BookingForm,ContactForm, ReviewForm

# Create your views here.
def make_booking(request):
    context={'bookings': Booking.objects.all()}
    context.update({'form':BookingForm})

    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'visitors_interface.html')
    return render(request, 'make_booking.html', context)

def visitors_page(request):
   vacancies= Vacancies.objects.all()
   return render(request,'visitors_interface.html',{'vacancies':vacancies})

def contact(request):
    context={'contact':Contact.objects.all()}
    context.update({'form':ContactForm})

    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visitors_homepage')
    return render(request, 'contact_us.html', context)


def review(request):
    context={'contact':Review.objects.all()}
    context.update({'form':ReviewForm})

    if request.method == 'POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visitors_homepage')
    return render(request, 'review.html', context)

def show_bookings(request):
    context={'bookings':Booking.objects.all()}
    return render(request, 'show_booking.html', context)

def show_booking_by_id(request,id:int):
    context={'booking':Booking.objects.get(id=id)}
    return render(request, 'show_booking_by_id.html', context)

def staff_interface(request):
    context=None
    return render(request, 'staff_interface.html',context)

def index (request):
    context = None
    return render(request,"index.html",context)
