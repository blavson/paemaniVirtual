# Generated by Django 2.0.4 on 2018-05-05 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suitor', '0009_remove_suitor_a'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aprnc',
            name='suitor_id',
        ),
        migrations.RemoveField(
            model_name='suitor',
            name='id',
        ),
        migrations.AddField(
            model_name='suitor',
            name='aprnc',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='suitor.Aprnc'),
            preserve_default=False,
        ),
    ]
