# Generated by Django 2.2.24 on 2021-12-03 18:18

from django.db import migrations, models
import django.utils.timezone
import social.models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0019_userprofile_credithour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventdate',
            field=models.DateTimeField(default=django.utils.timezone.now, validators=[social.models.validate_date]),
        ),
        migrations.AlterField(
            model_name='service',
            name='servicedate',
            field=models.DateTimeField(default=django.utils.timezone.now, validators=[social.models.validate_date]),
        ),
    ]
