# Generated by Django 2.2.24 on 2021-12-25 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0032_userprofile_unreadcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifyuser',
            name='offerPk',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='notifyuser',
            name='offerType',
            field=models.TextField(blank=True, null=True),
        ),
    ]