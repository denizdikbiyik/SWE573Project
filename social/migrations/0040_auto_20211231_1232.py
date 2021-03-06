# Generated by Django 2.2.24 on 2021-12-31 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0039_auto_20211231_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='requester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requester', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='toPerson',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='toPerson', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
