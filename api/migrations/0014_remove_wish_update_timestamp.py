# Generated by Django 2.1.7 on 2019-04-15 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20190415_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wish',
            name='update_timestamp',
        ),
    ]
