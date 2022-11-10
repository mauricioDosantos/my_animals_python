# Generated by Django 4.1.3 on 2022-11-10 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0006_alter_product_name_alter_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppinglist',
            old_name='end_date',
            new_name='ref_date',
        ),
        migrations.RemoveField(
            model_name='shoppinglist',
            name='animals',
        ),
        migrations.RemoveField(
            model_name='shoppinglist',
            name='start_date',
        ),
        migrations.AddField(
            model_name='shoppinglist',
            name='animal_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='animal.animal'),
            preserve_default=False,
        ),
    ]