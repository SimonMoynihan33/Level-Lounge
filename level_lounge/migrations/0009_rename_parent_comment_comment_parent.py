# Generated by Django 5.1 on 2024-09-10 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("level_lounge", "0008_rename_exercpt_post_excerpt"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="parent_comment",
            new_name="parent",
        ),
    ]
