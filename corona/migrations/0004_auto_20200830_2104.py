# Generated by Django 3.0.5 on 2020-08-30 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corona', '0003_auto_20200830_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coronadata',
            name='title',
        ),
        migrations.AddField(
            model_name='coronadata',
            name='total',
            field=models.CharField(default='', max_length=255),
        ),
    ]