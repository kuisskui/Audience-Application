# Generated by Django 4.2 on 2023-10-19 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0002_rename_year_userprofile_age_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='sport_ids',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='sport_ids',
            field=models.TextField(blank=True, null=True),
        ),
    ]
