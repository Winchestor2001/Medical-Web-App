# Generated by Django 4.1.4 on 2023-01-23 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0013_workstatus_staff_remove_workstatus_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workstatus',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]
