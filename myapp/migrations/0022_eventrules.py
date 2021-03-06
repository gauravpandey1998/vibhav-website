# Generated by Django 2.1.4 on 2018-12-30 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_auto_20181221_0602'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventRules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(default='', max_length=1500)),
                ('judging', models.CharField(default='', max_length=1500)),
                ('prizes', models.CharField(default='', max_length=1500)),
                ('contacts', models.CharField(default='', max_length=1500)),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.Event')),
            ],
        ),
    ]
