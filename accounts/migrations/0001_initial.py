# Generated by Django 4.2.7 on 2023-11-19 20:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "myshopify_domain",
                    models.CharField(editable=False, max_length=255, unique=True),
                ),
                (
                    "token",
                    models.CharField(
                        default="00000000000000000000000000000000",
                        editable=False,
                        max_length=64,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
