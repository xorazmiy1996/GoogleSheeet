# Generated by Django 4.1 on 2022-08-13 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googleSheet', '0003_alter_datas_price_in_rubles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datas',
            name='price_in_rubles',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
