# Generated by Django 4.1.4 on 2023-01-21 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0008_remove_work_street_work_street'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='date',
            field=models.DateField(),
        ),
    ]
