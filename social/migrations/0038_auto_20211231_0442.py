# Generated by Django 2.2.24 on 2021-12-31 04:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0037_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='toPerson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='toPerson', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
