# Generated by Django 4.0.4 on 2022-04-27 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_bom_label_bom_trim'),
    ]

    operations = [
        migrations.AddField(
            model_name='bom',
            name='graphic',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='graphic/'),
        ),
        migrations.AddField(
            model_name='bom',
            name='sketch',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='sketch/'),
        ),
    ]
