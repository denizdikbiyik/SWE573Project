# Generated by Django 2.2.24 on 2021-12-24 15:54

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0027_delete_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='-22.2876834,-49.1607606', max_length=63),
        ),
    ]
