from django.db import models
from datetime import datetime


class Address(models.Model):
	street = models.CharField(primary_key=True, max_length=75, blank=True)
	city = models.CharField(max_length=75, blank=True)
	state = models.CharField(max_length=25, blank=True)
	zip_code = models.CharField(max_length=25, blank=True)

class BasicInfo(models.Model):
	first_name = models.Charfield(primary_key=True, max_length=25)
	last_name = models.Charfield(max_length=50)
	email = models.Emailfield(max_length=50)
	cell_phone = models.CharField(max_length=25, unique=True)

class CreditCard(models.Model):
	cc_name = models.CharField(primary_key=True, max_length=150, blank=True)
	cc_num = models.CharField(max_length=16, unique=True)
	cc_exp= models.DateField()#(blank=True)
	cc_zip = models.CharField(max_length=25)
	cc_scode = models.CharField(max_length=6)

class DriverLicense(models.Model):
	dl_num = models.CharField(primary_key=True, max_length=25, blank=True, unique=True)
	dl_exp = models.DateField()#(blank=True)
	dl_dob = models.DateField()#(blank=True)

class FlightItinerary(models.Model):
	arriving_airport = models.CharField(max_length=125, blank=True)
	arriving_airline = models.CharField(max_length=125, blank=True)
	arriving_flight_number = models.CharField(max_length=25, blank=True)
	arriving_date_time = models.DateTimeField(blank=True)
	departing_airport = models.CharField(max_length=125, blank=True)
	departing_airline = models.CharField(max_length=125, blank=True)
	departing_flight_number = models.CharField(max_length=25, blank=True)
	departing_date_time = models.DateTimeField(blank=True)

class Organization(models.Model):
	org_name = models.CharField(max_length=50)
	org_address = models.ForeignKey(Address, on_delete='CASCADE', blank=True,  null=True)
	org_representative = models.ForeignKey(BasicInfo, on_delete='CASCADE', blank=True,  null=True)

class StatementOfCHarges(models.Model):
	num_of_vans = models.IntegerField(blank=True)
	rate_charge = models.IntegerField(blank=True)
	mileage_over_charge = models.IntegerField(blank=True)
	late_charge = models.IntegerField(blank=True)
	fuel_charge = models.IntegerField(blank=True)
	damage_charge = models.IntegerField(blank=True)
	additional_driver = models.IntegerField(blank=True)
	under_age = models.IntegerField(blank=True)
	drop_fee = models.IntegerField(blank=True)
	mexico_insurance = models.IntegerField(blank=True)
	cleaning_fee = models.IntegerField(blank=True)
	other_charges = models.IntegerField(blank=True)
	surcharge = models.IntegerField(blank=True)
	license_tax = models.IntegerField(blank=True)
	sales_tax = models.IntegerField(blank=True)
	airport_access_fee = models.IntegerField(blank=True)
	subtotal_out = models.IntegerField(blank=True)
	total_due = models.IntegerField(blank=True)
	subtotal_in = models.IntegerField(blank=True)
	grand_total = models.IntegerField(blank=True)

class Customer(models.Model):
	org_info = models.ForeignKey(Organization, on_delete='CASCADE', blank=True,  null=True)
	primary_info = models.ForeignKey(BasicInfo, on_delete='CASCADE', blank=True,  null=True)
	address = models.ForeignKey(Address, on_delete='CASCADE', blank=True,  null=True)
	drivers_license = models.ForeignKey(DriverLicense, on_delete='CASCADE', blank=True, null=True)
	credit_card = models.ForeignKey(CreditCard, on_delete='CASCADE', blank=True, null=True)