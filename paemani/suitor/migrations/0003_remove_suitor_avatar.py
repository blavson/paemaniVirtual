# Generated by Django 2.0.4 on 2018-05-04 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suitor', '0002_auto_20180504_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suitor',
            name='avatar',
        ),
    ]