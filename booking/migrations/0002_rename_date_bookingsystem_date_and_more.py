# Generated by Django 4.2.11 on 2024-04-24 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingsystem',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='bookingsystem',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='bookingsystem',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='bookingsystem',
            old_name='Number_Of_People',
            new_name='number_of_people',
        ),
        migrations.RenameField(
            model_name='bookingsystem',
            old_name='Phone_number',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='bookingsystem',
            old_name='Time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='bookingsystem',
            old_name='User',
            new_name='user',
        ),
    ]
