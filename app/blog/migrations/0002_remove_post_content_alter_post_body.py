# Generated by Django 4.2.3 on 2023-07-25 08:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="content",
        ),
        migrations.AlterField(
            model_name="post",
            name="body",
            field=models.TextField(max_length=1000),
        ),
    ]