# Generated by Django 2.2.24 on 2021-11-20 16:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='servicedate',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 16, 1, 36, 2759)),
            preserve_default=False,
        ),
    ]
