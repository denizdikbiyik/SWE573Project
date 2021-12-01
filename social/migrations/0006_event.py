# Generated by Django 2.2.24 on 2021-11-21 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0005_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventcreateddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('eventname', models.TextField()),
                ('eventdescription', models.TextField()),
                ('eventpicture', models.ImageField(blank=True, default='uploads/event_pictures/default.png', upload_to='uploads/event_pictures/')),
                ('eventlocation', models.CharField(blank=True, max_length=100, null=True)),
                ('eventdate', models.DateTimeField(default=django.utils.timezone.now)),
                ('eventcapacity', models.IntegerField()),
                ('eventcreater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]