# Generated by Django 2.2.24 on 2021-12-25 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0031_notifyuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='unreadcount',
            field=models.IntegerField(default=0),
        ),
    ]
