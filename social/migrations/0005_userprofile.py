# Generated by Django 2.2.24 on 2021-11-21 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('social', '0004_auto_20211120_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('picture', models.ImageField(blank=True, default='uploads/profile_pictures/default.png', upload_to='uploads/profile_pictures/')),
            ],
        ),
    ]
