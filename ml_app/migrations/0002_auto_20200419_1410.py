# Generated by Django 3.0.5 on 2020-04-19 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titanicdb',
            name='nn_result',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='titanicdb',
            name='skl_result',
            field=models.CharField(default='0', max_length=3),
        ),
    ]
