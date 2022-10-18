# Generated by Django 3.0.3 on 2022-10-18 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buyers', '0007_auto_20221018_1006'),
        ('plots', '0003_auto_20221017_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='plot_number',
            name='bookedby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buyers.BuyerInfo'),
        ),
    ]