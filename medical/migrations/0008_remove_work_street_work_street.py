# Generated by Django 4.1.4 on 2023-01-20 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0007_work_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='street',
        ),
        migrations.AddField(
            model_name='work',
            name='street',
            field=models.ManyToManyField(to='medical.street'),
        ),
    ]
