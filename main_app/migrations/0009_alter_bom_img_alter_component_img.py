# Generated by Django 4.0.4 on 2022-04-23 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_bom_img_alter_component_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bom',
            name='img',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='component',
            name='img',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='media/'),
        ),
    ]
