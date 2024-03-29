# Generated by Django 2.2.5 on 2019-11-06 02:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(blank=True, max_length=75)),
                ('city', models.CharField(blank=True, max_length=75)),
                ('state', models.CharField(blank=True, max_length=25)),
                ('zip_code', models.CharField(blank=True, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='AdobeVanInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('van_id', models.CharField(max_length=25)),
                ('van_year_make_model', models.CharField(max_length=100)),
                ('van_vin', models.CharField(max_length=25)),
                ('van_plate', models.CharField(max_length=25)),
                ('van_size', models.CharField(max_length=25)),
                ('mileage_start', models.CharField(blank=True, max_length=25)),
                ('mileage_end', models.CharField(blank=True, max_length=25)),
                ('van_reg_exp', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ArrivingDepartingFlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arriving_airport', models.CharField(blank=True, max_length=125)),
                ('arriving_airline', models.CharField(blank=True, max_length=125)),
                ('arriving_flight_number', models.CharField(blank=True, max_length=25)),
                ('arriving_date_time', models.DateTimeField(blank=True)),
                ('departing_airport', models.CharField(blank=True, max_length=125)),
                ('departing_airline', models.CharField(blank=True, max_length=125)),
                ('departing_flight_number', models.CharField(blank=True, max_length=25)),
                ('departing_date_time', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc_name', models.CharField(blank=True, max_length=150)),
                ('cc_num', models.CharField(max_length=16, unique=True)),
                ('cc_exp', models.DateField()),
                ('cc_zip', models.CharField(max_length=25)),
                ('cc_scode', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DriverLicense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dl_num', models.CharField(blank=True, max_length=25, unique=True)),
                ('dl_exp', models.DateField()),
                ('dl_dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('cell_phone', models.CharField(max_length=25, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cust_address', models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='adobe_app.Address')),
                ('cust_credit_card', models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='adobe_app.CreditCard')),
                ('cust_driver_license', models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='adobe_app.DriverLicense')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('org_id', models.AutoField(primary_key=True, serialize=False)),
                ('org_name', models.CharField(max_length=50)),
                ('dl_num', models.CharField(blank=True, max_length=25)),
                ('dl_exp', models.DateTimeField(blank=True)),
                ('dl_dob', models.DateTimeField(blank=True)),
                ('cc_num', models.CharField(blank=True, max_length=16)),
                ('cc_exp', models.DateTimeField(blank=True)),
                ('cc_zip', models.CharField(blank=True, max_length=25)),
                ('org_address', models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='adobe_app.Address')),
                ('org_representative', models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='adobe_app.Individual')),
            ],
        ),
        migrations.CreateModel(
            name='RentalAgreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='RentalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_title', models.CharField(max_length=200)),
                ('tutorial_content', models.TextField()),
                ('tutorial_published', models.DateTimeField(default=datetime.datetime.now, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VanRental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_date_start', models.DateTimeField(blank=True)),
                ('rental_date_end', models.DateTimeField(blank=True)),
                ('num_of_vans', models.IntegerField(blank=True)),
                ('rate_charge', models.IntegerField(blank=True)),
                ('mileage_over_charge', models.IntegerField(blank=True)),
                ('late_charge', models.IntegerField(blank=True)),
                ('fuel_charge', models.IntegerField(blank=True)),
                ('damage_charge', models.IntegerField(blank=True)),
                ('additional_driver', models.IntegerField(blank=True)),
                ('under_age', models.IntegerField(blank=True)),
                ('drop_fee', models.IntegerField(blank=True)),
                ('mexico_insurance', models.IntegerField(blank=True)),
                ('cleaning_fee', models.IntegerField(blank=True)),
                ('other_charges', models.IntegerField(blank=True)),
                ('surcharge', models.IntegerField(blank=True)),
                ('license_tax', models.IntegerField(blank=True)),
                ('sales_tax', models.IntegerField(blank=True)),
                ('airport_access_fee', models.IntegerField(blank=True)),
                ('subtotal_out', models.IntegerField(blank=True)),
                ('total_due', models.IntegerField(blank=True)),
                ('subtotal_in', models.IntegerField(blank=True)),
                ('grand_total', models.IntegerField(blank=True)),
                ('org_name', models.ForeignKey(blank=True, on_delete='CASCADE', to='adobe_app.Organization')),
                ('vans_assigned', models.ForeignKey(blank=True, on_delete='CASCADE', to='adobe_app.AdobeVanInfo')),
            ],
        ),
        migrations.CreateModel(
            name='CommentBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2019, 11, 5, 19, 30, 15, 444684), verbose_name='Date of Entry')),
                ('comments', models.TextField()),
                ('comment_by', models.ForeignKey(on_delete='CASCADE', to='adobe_app.VanRental')),
                ('rental_info', models.ForeignKey(on_delete='CASCADE', to='adobe_app.RentalInfo')),
            ],
        ),
        migrations.CreateModel(
            name='AdobeDriver',
            fields=[
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('cell_phone', models.CharField(max_length=25, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='adobe_app.Address')),
                ('driver_license', models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='adobe_app.DriverLicense')),
            ],
        ),
        migrations.CreateModel(
            name='AdditionalDriver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=125)),
                ('dl_info', models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='adobe_app.DriverLicense')),
            ],
        ),
    ]
