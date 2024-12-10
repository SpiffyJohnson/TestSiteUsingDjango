# Generated by Django 5.1.3 on 2024-11-19 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('cNumber', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gpa', models.FloatField()),
            ],
        ),
    ]
