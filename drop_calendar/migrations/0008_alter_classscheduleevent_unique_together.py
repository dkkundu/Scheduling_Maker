# Generated by Django 3.2 on 2021-07-01 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drop_calendar', '0007_auto_20210701_1340'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='classscheduleevent',
            unique_together=set(),
        ),
    ]
