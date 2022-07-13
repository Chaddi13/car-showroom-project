# Generated by Django 4.0.6 on 2022-07-11 16:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer_app', '0001_initial'),
        ('shipper_app', '0001_initial'),
        ('showroom_app', '0001_initial'),
        ('car_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesShowroomToCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('amount_of_discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30)])),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sold_car', to='car_app.car')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='customer_transaction_history', to='customer_app.customer')),
                ('showroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='showroom', to='showroom_app.showroom')),
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
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('amount_of_discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30)])),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='car_for_sale', to='car_app.car')),
                ('shipper', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='shipper_that_sells', to='shipper_app.shipper')),
                ('showroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='showroom_that_buys', to='showroom_app.showroom')),
            ],
            options={
                'db_table': 'sales_dealer_to_showroom',
            },
        ),
    ]
