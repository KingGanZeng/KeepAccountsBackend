# Generated by Django 2.1.7 on 2019-04-20 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20190416_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='book_type',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
