# Generated by Django 3.2.7 on 2021-12-06 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0008_alter_doctorschedule_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorschedule',
            name='day',
            field=models.CharField(choices=[('Friday ', 'Friday '), ('Monday', 'Monday'), ('Wednesday', 'Wednesday'), ('Tuesday', 'Tuesday'), ('Saturday', 'Saturday'), ('Thursday', 'Thursday'), ('Sunday', 'Sunday')], default='Saturday', max_length=100),
        ),
    ]
