# Generated by Django 2.1.4 on 2018-12-20 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20181220_0305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='event',
        ),
    ]
