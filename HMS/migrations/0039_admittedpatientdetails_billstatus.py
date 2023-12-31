# Generated by Django 4.1.7 on 2023-06-18 11:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("HMS", "0038_admittedpatientdetails_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="admittedpatientdetails",
            name="billStatus",
            field=models.CharField(
                choices=[("PENDING", "PENDING"), ("PAID", "PAID")],
                default="PENDING",
                max_length=15,
            ),
        ),
    ]
