# Generated by Django 5.0.1 on 2024-02-06 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='defect',
            name='d_reported_by',
        ),
        migrations.RemoveField(
            model_name='user',
            name='u_access',
        ),
        migrations.AddField(
            model_name='user',
            name='a_access',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='admin',
            name='a_access',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='defect',
            name='d_status',
            field=models.CharField(choices=[('Прийнято', 'PRIJNATO'), ('Виконано', 'VYKONANO'), ('В обробці', 'V_OBROBCI'), ('Відхилено', 'VIDHYLENO')], max_length=45),
        ),
        migrations.AlterField(
            model_name='order',
            name='o_status',
            field=models.CharField(choices=[('Прийнято', 'PRIJNATO'), ('Виконано', 'VYKONANO'), ('В обробці', 'V_OBROBCI'), ('Відхилено', 'VIDHYLENO')], max_length=45),
        ),
    ]
