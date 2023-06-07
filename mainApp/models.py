from django.db import models
from datetime import date
from django import forms
from django.core.validators import RegexValidator, EmailValidator


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

GENDER_CHOICES = (
   ('Male', 'Male'),
   ('Female', 'Female'),
   ('Other', 'Other')
)




class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=30, validators=[RegexValidator(r'^[a-zA-Z]+$', message='First name must contain alphabets only')])
    lastname = models.CharField(max_length=30, validators=[RegexValidator(r'^[a-zA-Z]+$', message='First name must contain alphabets only')])
    email = models.EmailField(validators=[EmailValidator(message='Please enter a valid email address')],default="", null=True )
    country = models.CharField(max_length=50, default='', null=True)
    state = models.CharField(max_length=50, default='', null=True)
    city = models.CharField(max_length=50, default='', null=True)
    dob = models.DateField(max_length=12,null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=12,null=True)
    age = models.CharField(max_length=30, default="", null=True)
    # DisplayFields = [id, firstname, lastname, dob , age]

    def __str__(self):
        return str(self.id)+" / "+self.firstname+" / "+self.lastname


