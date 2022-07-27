# Generated by Django 4.0.6 on 2022-07-20 13:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('showroom', '0001_initial'),
        ('customer', '0001_initial'),
        ('car', '0001_initial'),
        ('shipper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesShowroomToCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('amount_of_discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30)])),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sold_car', to='car.car')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='customer_transaction_history', to='customer.customer')),
                ('showroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='showroom', to='showroom.showroom')),
            ],
            options={
                'db_table': 'sales_showroom_to_customer',
            },
        ),
        migrations.CreateModel(
            name='SalesShipperToShowroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('amount_of_discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30)])),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='car_for_sale', to='car.car')),
                ('shipper', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='shipper_that_sells', to='shipper.shipper')),
                ('showroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='showroom_that_buys', to='showroom.showroom')),
            ],
            options={
                'db_table': 'sales_shipper_to_showroom',
            },
        ),
    ]
