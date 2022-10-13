# Generated by Django 4.1.2 on 2022-10-12 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("applicants", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="applicant",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="addresses",
                to="applicants.applicant",
            ),
        ),
        migrations.AlterField(
            model_name="applicant",
            name="pob",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="applicants.country",
                verbose_name="place of birth",
            ),
        ),
    ]
