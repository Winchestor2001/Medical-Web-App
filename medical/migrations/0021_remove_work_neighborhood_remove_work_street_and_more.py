# Generated by Django 4.1.4 on 2023-01-23 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0020_remove_workstatus_address_remove_workstatus_doctor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='neighborhood',
        ),
        migrations.RemoveField(
            model_name='work',
            name='street',
        ),
        migrations.AddField(
            model_name='work',
            name='address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='medical.address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]
