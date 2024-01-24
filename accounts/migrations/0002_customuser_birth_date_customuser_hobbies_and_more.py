# Generated by Django 4.2.8 on 2024-01-06 07:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="birth_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="hobbies",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="customuser",
            name="nickname",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]