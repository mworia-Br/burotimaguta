# Generated by Django 3.2.15 on 2022-10-15 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plots', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plot',
            name='deposit',
            field=models.IntegerField(null=True),
        ),
    ]
