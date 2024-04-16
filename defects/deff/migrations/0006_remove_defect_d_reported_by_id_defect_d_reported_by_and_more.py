# Generated by Django 5.0.1 on 2024-02-09 09:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deff', '0005_defect_d_reported_by_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='defect',
            name='d_reported_by_id',
        ),
        migrations.AddField(
            model_name='defect',
            name='d_reported_by',
            field=models.ForeignKey(db_column='d_reported_by', default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='deff.user'),
        ),
        migrations.AlterField(
            model_name='defect',
            name='d_status',
            field=models.CharField(choices=[('Прийнято', 'accepted'), ('Виконано', 'completed'), ('В обробці', 'in_progress'), ('Відхилено', 'rejected')], max_length=45),
        ),
        migrations.AlterField(
            model_name='order',
            name='o_status',
            field=models.CharField(choices=[('Прийнято', 'accepted'), ('Виконано', 'completed'), ('В обробці', 'in_progress'), ('Відхилено', 'rejected')], max_length=45),
        ),
    ]
