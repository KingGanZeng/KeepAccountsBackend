# Generated by Django 2.1.7 on 2019-04-08 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_book_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='group_id_array',
        ),
    ]