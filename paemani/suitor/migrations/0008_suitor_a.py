# Generated by Django 2.0.4 on 2018-05-05 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suitor', '0007_auto_20180505_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='suitor',
            name='a',
            field=models.IntegerField(default=0),
        ),
    ]
