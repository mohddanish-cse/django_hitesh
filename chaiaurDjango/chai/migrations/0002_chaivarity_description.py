# Generated by Django 5.1.2 on 2024-10-14 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chai", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="chaivarity",
            name="description",
            field=models.TextField(default=""),
        ),
    ]
