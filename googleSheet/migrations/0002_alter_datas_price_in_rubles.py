# Generated by Django 4.1 on 2022-08-13 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googleSheet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datas',
            name='price_in_rubles',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
