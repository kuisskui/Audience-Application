# Generated by Django 4.2 on 2023-10-19 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audience', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='year',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='country_id',
            new_name='country',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='sport_ids',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='sport_ids',
            field=models.ManyToManyField(to='audience.sport'),
        ),
    ]
