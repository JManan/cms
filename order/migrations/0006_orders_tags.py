# Generated by Django 4.1.5 on 2023-03-23 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0005_orders_favorites"),
    ]

    operations = [
        migrations.AddField(
            model_name="orders",
            name="tags",
            field=models.CharField(
                choices=[
                    ("electronics", "electronics"),
                    ("furniture", "furniture"),
                    ("food", "food"),
                    ("stationary", "stationary"),
                    ("beverages", "beverages"),
                    ("other", "other"),
                ],
                default="other",
                max_length=20,
            ),
        ),
    ]