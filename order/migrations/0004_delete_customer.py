# Generated by Django 4.1.5 on 2023-03-20 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0003_customer"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Customer",
        ),
    ]
