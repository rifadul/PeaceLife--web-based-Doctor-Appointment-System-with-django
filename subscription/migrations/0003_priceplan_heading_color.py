# Generated by Django 3.2.7 on 2021-12-07 06:45

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0002_priceplan_plan_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='priceplan',
            name='heading_color',
            field=colorfield.fields.ColorField(default='#07d5c0', max_length=18, samples=None),
        ),
    ]
