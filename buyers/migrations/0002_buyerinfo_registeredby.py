# Generated by Django 3.2.15 on 2022-10-15 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyerinfo',
            name='registeredBy',
            field=models.CharField(max_length=15, null=True),
        ),
    ]