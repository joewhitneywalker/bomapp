# Generated by Django 4.0.4 on 2022-04-27 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_trim'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=200)),
                ('article_code', models.CharField(max_length=50)),
                ('supplier', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, max_length=255, null=True, upload_to='labels/')),
                ('cost', models.CharField(max_length=50)),
                ('material_compostition', models.CharField(max_length=200)),
            ],
        ),
    ]
