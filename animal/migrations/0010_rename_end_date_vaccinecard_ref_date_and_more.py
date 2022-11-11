# Generated by Django 4.1.3 on 2022-11-10 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0009_alter_tasklist_animal_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vaccinecard',
            old_name='end_date',
            new_name='ref_date',
        ),
        migrations.RemoveField(
            model_name='vaccinecard',
            name='animals',
        ),
        migrations.RemoveField(
            model_name='vaccinecard',
            name='start_date',
        ),
        migrations.AddField(
            model_name='vaccinecard',
            name='animal_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='animal.animal'),
        ),
    ]
