from django.db import models

class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    number_of_person=models.IntegerField()
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    booking_date = models.DateField()
    additional_info = models.TextField()
    def __str__(self) :
        return f'{self.first_name} {self.last_name}'

class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length= 20)
    address = models.CharField(max_length=100)
    date_join = models.DateField()
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Review(models.Model):
    email = models.EmailField()
    text = models.TextField()
    def __str__(self):
        return f'{self.email}'

class Room(models.Model):
    rt = [("std","Standard"),("de","Delux"),("sin","Single"),("db","Double")]
    room_trype = models.CharField(max_length=3, choices = rt)
    price = models.IntegerField()
    status = models.BooleanField( default= False)
    def __str__(self):
        return f'{self.room_trype} {self.price}'

class Vacancies(models.Model):
    September=models.DateField()
    October=models.DateField()
    November=models.DateField()

class Contact(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    questions=models.TextField()





        


