# Generated by Django 4.1.7 on 2023-03-05 05:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tree_menu", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="url",
            field=models.CharField(default="", editable=False, max_length=300),
            preserve_default=False,
        ),
    ]
