# Generated by Django 5.1.1 on 2024-09-10 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_person_death_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='name',
        ),
    ]
