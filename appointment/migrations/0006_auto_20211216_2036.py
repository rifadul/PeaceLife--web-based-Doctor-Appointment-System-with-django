# Generated by Django 3.2.7 on 2021-12-16 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_auto_20211212_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='confirmation_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accept', 'Accept'), ('Reject', 'Reject')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='gender',
            field=models.CharField(choices=[('Other', 'Other'), ('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=100),
        ),
    ]