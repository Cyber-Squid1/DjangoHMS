# Generated by Django 4.1.7 on 2023-06-11 18:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("HMS", "0005_feedback"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="patientUsername",
            field=models.CharField(default="", max_length=200),
        ),
    ]
