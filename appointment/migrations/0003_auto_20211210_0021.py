# Generated by Django 3.2.7 on 2021-12-09 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_auto_20211210_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='confirmation_status',
            field=models.CharField(choices=[('Reject', 'Reject'), ('Accept', 'Accept'), ('Pending', 'Pending')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=100),
        ),
    ]
