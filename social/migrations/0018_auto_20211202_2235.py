# Generated by Django 2.2.24 on 2021-12-02 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0017_auto_20211201_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='eventduration',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='service',
            name='duration',
            field=models.IntegerField(default=1),
        ),
    ]
