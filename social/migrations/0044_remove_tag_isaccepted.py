# Generated by Django 2.2.24 on 2021-12-31 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0043_auto_20211231_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='isAccepted',
        ),
    ]
