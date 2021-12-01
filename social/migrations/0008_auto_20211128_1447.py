# Generated by Django 2.2.24 on 2021-11-28 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_userprofile_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='creater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creater', to=settings.AUTH_USER_MODEL),
        ),
    ]