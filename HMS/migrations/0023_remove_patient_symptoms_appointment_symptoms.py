# Generated by Django 4.1.7 on 2023-06-13 05:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("HMS", "0022_rename_doctoridid_admittedpatientdetails_doctorid_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="patient",
            name="symptoms",
        ),
        migrations.AddField(
            model_name="appointment",
            name="symptoms",
            field=models.CharField(default="", max_length=1000),
        ),
    ]
