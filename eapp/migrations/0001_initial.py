# Generated by Django 3.0.8 on 2020-07-03 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('type', models.IntegerField(choices=[(1, 'Sedan'), (2, 'Truck'), (4, 'SUV')])),
            ],
        ),
    ]
