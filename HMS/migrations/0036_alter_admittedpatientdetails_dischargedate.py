# Generated by Django 4.1.7 on 2023-06-17 12:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("HMS", "0035_alter_admittedpatientdetails_dischargedate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="admittedpatientdetails",
            name="dischargeDate",
            field=models.DateField(null=True),
        ),
    ]
