# Generated by Django 3.2.7 on 2021-12-24 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0021_alter_doctorschedule_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorschedule',
            name='day',
            field=models.CharField(choices=[('Tuesday', 'Tuesday'), ('Sunday', 'Sunday'), ('Friday ', 'Friday '), ('Thursday', 'Thursday'), ('Monday', 'Monday'), ('Wednesday', 'Wednesday'), ('Saturday', 'Saturday')], default='Saturday', max_length=100),
        ),
    ]
