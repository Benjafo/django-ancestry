# Generated by Django 5.1.1 on 2024-09-09 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('file_location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birth_date', models.DateField()),
                ('death_date', models.DateField()),
                ('events', models.ManyToManyField(to='api.event')),
                ('sources', models.ManyToManyField(to='api.source')),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='members', to='api.tree')),
            ],
        ),
    ]
