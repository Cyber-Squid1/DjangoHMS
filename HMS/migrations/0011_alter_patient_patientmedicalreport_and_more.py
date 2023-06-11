# Generated by Django 4.1.7 on 2023-06-11 18:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("HMS", "0010_alter_patient_patientprofileimg"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="patientMedicalReport",
            field=models.ImageField(
                default="", upload_to="patientMedicalReports/<int:Patient.pk>"
            ),
        ),
        migrations.AlterField(
            model_name="patient",
            name="symptoms",
            field=models.CharField(default="", max_length=1000),
        ),
    ]
