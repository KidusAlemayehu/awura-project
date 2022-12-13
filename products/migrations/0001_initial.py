# Generated by Django 4.1.3 on 2022-12-03 01:52

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('spec', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('main_image', models.FileField(default=None, upload_to=products.models.directory_path)),
                ('quantity', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Products',
            },
        ),
    ]
