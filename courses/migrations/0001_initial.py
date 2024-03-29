# Generated by Django 3.0 on 2021-04-29 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=70)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("number_of_lectures", models.IntegerField()),
            ],
        ),
    ]
