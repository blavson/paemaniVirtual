# Generated by Django 2.0.4 on 2018-05-04 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suitor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aprnc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ethnicity', models.CharField(choices=[('white', 'White/Caucasian'), ('black', 'Black'), ('latino', 'Latino'), ('asian', 'Asian'), ('native', 'Native Indian')], default='white', max_length=10)),
                ('hair', models.CharField(choices=[('black', 'BLACK'), ('grey', 'GREY'), ('brown', 'BROWN'), ('bald', 'BALD')], default='black', max_length=6)),
                ('width', models.IntegerField(default=0)),
                ('weight', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='characteristics',
            name='suitor_id',
        ),
        migrations.AddField(
            model_name='suitor',
            name='avatar',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='suitor',
            name='age',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Characteristics',
        ),
        migrations.AddField(
            model_name='aprnc',
            name='suiter_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='suitor.Suitor'),
        ),
    ]
