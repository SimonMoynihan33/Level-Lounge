# Generated by Django 5.1 on 2024-09-19 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("level_lounge", "0012_rename_created_at_userprofile_joined_on_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="profile_picture",
            field=models.ImageField(blank=True, null=True, upload_to="profile_pics/"),
        ),
    ]
