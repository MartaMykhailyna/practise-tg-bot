# Generated by Django 5.0.1 on 2024-02-08 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deff', '0004_remove_admin_id_remove_defect_id_remove_order_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='defect',
            name='d_reported_by_id',
            field=models.ForeignKey(db_column='d_reported_by', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='deff.user'),
        ),
    ]
