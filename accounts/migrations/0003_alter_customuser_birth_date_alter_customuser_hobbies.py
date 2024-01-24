# Generated by Django 4.2.8 on 2024-01-06 08:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_customuser_birth_date_customuser_hobbies_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="birth_date",
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="hobbies",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]