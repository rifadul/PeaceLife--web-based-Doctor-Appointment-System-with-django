# Generated by Django 3.2.7 on 2021-12-03 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_auto_20211203_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorschedule',
            name='day',
            field=models.CharField(choices=[('Sunday', 'Sunday'), ('Saturday', 'Saturday'), ('Wednesday', 'Wednesday'), ('Tuesday', 'Tuesday'), ('Monday', 'Monday'), ('Friday ', 'Friday '), ('Thursday', 'Thursday')], default='Saturday', max_length=100),
        ),
    ]