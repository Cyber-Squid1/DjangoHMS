# Generated by Django 4.1.7 on 2023-06-17 17:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("HMS", "0037_remove_admittedpatientdetails_doctorfees_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="admittedpatientdetails",
            name="status",
            field=models.CharField(
                choices=[("ADMITTED", "ADMITTED"), ("DISCHARGED", "DISCHARGED")],
                default="ADMITTED",
                max_length=15,
            ),
        ),
    ]
