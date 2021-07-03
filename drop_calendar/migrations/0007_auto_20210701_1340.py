# Generated by Django 3.2 on 2021-07-01 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drop_calendar', '0006_alter_classscheduleevent_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classscheduleevent',
            name='end_date',
            field=models.DateTimeField(null=True, verbose_name='End Time'),
        ),
        migrations.AlterField(
            model_name='classscheduleevent',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name='Subject'),
        ),
        migrations.AlterField(
            model_name='classscheduleevent',
            name='start_date',
            field=models.DateTimeField(null=True, verbose_name='Start Time'),
        ),
    ]
