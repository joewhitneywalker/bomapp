# Generated by Django 4.0.4 on 2022-04-28 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_label_quantity_label_usage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trim',
            name='quantity',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='1', max_length=10),
        ),
    ]