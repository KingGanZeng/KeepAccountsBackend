# Generated by Django 2.1.7 on 2019-03-19 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20190319_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='note',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
