# Generated by Django 2.2.24 on 2021-12-31 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0038_auto_20211231_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='toPerson',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
