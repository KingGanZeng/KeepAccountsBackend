# Generated by Django 2.1.7 on 2019-03-19 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190319_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='note',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
