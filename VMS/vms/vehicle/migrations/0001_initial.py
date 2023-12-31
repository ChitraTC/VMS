# Generated by Django 4.0.8 on 2023-08-09 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_number', models.CharField(max_length=50)),
                ('vehicle_type', models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4')], default='2', max_length=50)),
                ('vehicle_model', models.CharField(max_length=200)),
                ('vehicle_description', models.TextField()),
            ],
        ),
    ]
