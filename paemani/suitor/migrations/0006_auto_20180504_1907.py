# Generated by Django 2.0.4 on 2018-05-04 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suitor', '0005_auto_20180504_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aprnc',
            old_name='hair',
            new_name='hair_color',
        ),
    ]
