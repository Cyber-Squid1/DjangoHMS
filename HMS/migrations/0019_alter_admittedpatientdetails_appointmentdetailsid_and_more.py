# Generated by Django 4.1.7 on 2023-06-12 17:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("HMS", "0018_alter_admittedpatientdetails_appointmentdetailsid_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="admittedpatientdetails",
            name="appointmentDetailsId",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="admittedpatientdetails",
            name="doctorIdId",
            field=models.CharField(default="", max_length=10),
        ),
        migrations.AlterField(
            model_name="admittedpatientdetails",
            name="patientId",
            field=models.CharField(default="", max_length=10),
        ),
    ]
