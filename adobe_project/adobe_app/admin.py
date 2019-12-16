from django.contrib import admin
from .models import User, Address, DriverLicense, AdobeVanInfo, CreditCard, AdditionalDriver, ArrivingDepartingFlight, VanRental, Individual, Organization, RentalInfo, CommentBox, Tutorial, AdobeDriver
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

admin.site.register(User)
admin.site.register(Tutorial)
admin.site.register(Address)
admin.site.register(DriverLicense)
admin.site.register(CreditCard)
admin.site.register(AdditionalDriver)
admin.site.register(ArrivingDepartingFlight)
admin.site.register(AdobeVanInfo)
admin.site.register(VanRental)
admin.site.register(Individual)
admin.site.register(Organization)
admin.site.register(RentalInfo)
admin.site.register(AdobeDriver)

class CommentBoxAdmin(admin.ModelAdmin):
	fieldsets = [
		("Main Info", {"fields": ["comment_by", "rental_info", "timestamp"]}),
		("Comments", {"fields": ["comments"]})
	]

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
	}

admin.site.register(CommentBox, CommentBoxAdmin)
'''
Address
DriverLicense
CreditCard
AdditionalDriver
ArrivingFlight
DepartingFlight
VanRental
Individual
Organization
RentalInfo
CommentBox
Individual
'''