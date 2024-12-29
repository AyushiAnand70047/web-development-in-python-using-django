# Generated by Django 5.1.4 on 2024-12-29 15:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ChaiVarity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="chais/")),
                ("date_added", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("MT", "Masala Tea"),
                            ("AT", "Adrak Tea"),
                            ("GT", "Green Tea"),
                            ("CT", "Cardamom Tea"),
                            ("BT", "Black Tea"),
                        ],
                        max_length=2,
                    ),
                ),
            ],
        ),
    ]
