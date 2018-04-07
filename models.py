from __future__ import unicode_literals
from datetime import date
from django.utils import timezone
from django.db import models


class Doctor(models.Model):
	name = models.CharField(max_length = 100)
	age = models.PositiveIntegerField()
	address = models.CharField(max_length = 100)
	mobile_no = models.PositiveIntegerField()
	salary = models.PositiveIntegerField()
	speacialisation = models.CharField(max_length = 200) 


class Patient(models.Model):
	is_valid = models.BooleanField(default = False)


class Appointment(models.Model):
	date = models.DateField(default = date.today)
	Time = models.TimeField()
	doctor_id = models.ForeignKey(Doctor, on_delete = models.CASCADE)
	patient_index = models.ForeignKey(Patient, on_delete = models.CASCADE)


class Payment(models.Model):
	details = models.CharField(max_length = 1000)
	method = models.CharField(max_length = 100)
	patient_index = models.ForeignKey(Patient, on_delete = models.CASCADE)


class Bill(models.Model):
	total = models.PositiveIntegerField()
	meds = models.CharField(max_length = 1000)
	doctor_id = models.ForeignKey(Doctor, on_delete = models.CASCADE)


# http://www.javaguicodexample.com/erdrelationalmodelnotes2.html