# Generated by Django 4.1.3 on 2022-11-08 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0003_alter_animal_people_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='tasks',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='vaccines',
        ),
    ]
