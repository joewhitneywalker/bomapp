# Generated by Django 4.0.4 on 2022-04-29 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0025_remove_bom_graphic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='component',
            old_name='material_compostition',
            new_name='material_composition',
        ),
        migrations.RenameField(
            model_name='label',
            old_name='material_compostition',
            new_name='material_composition',
        ),
        migrations.RenameField(
            model_name='trim',
            old_name='material_compostition',
            new_name='material_composition',
        ),
    ]
