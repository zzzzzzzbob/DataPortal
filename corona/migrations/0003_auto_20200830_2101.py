# Generated by Django 3.0.5 on 2020-08-30 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corona', '0002_auto_20200830_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coronadata',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
