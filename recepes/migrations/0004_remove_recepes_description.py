# Generated by Django 3.1.13 on 2021-08-12 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepes', '0003_auto_20210812_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recepes',
            name='description',
        ),
    ]
