# Generated by Django 3.2.7 on 2021-12-06 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pecelife', '0008_rename_questions_frequentlyquestion_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_class_name', models.CharField(max_length=255)),
                ('service_name', models.CharField(max_length=255)),
                ('about_service', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]