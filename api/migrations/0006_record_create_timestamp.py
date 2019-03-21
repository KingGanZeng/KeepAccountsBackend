# Generated by Django 2.1.7 on 2019-03-20 14:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_book_create_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='create_timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]