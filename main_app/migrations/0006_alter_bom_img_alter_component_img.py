# Generated by Django 4.0.4 on 2022-04-23 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_bom_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bom',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='component',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
