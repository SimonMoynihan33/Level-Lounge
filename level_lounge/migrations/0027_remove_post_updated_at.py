# Generated by Django 5.1 on 2024-09-26 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("level_lounge", "0026_post_updated_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="updated_at",
        ),
    ]
