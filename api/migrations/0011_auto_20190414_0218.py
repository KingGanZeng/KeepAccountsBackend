# Generated by Django 2.1.7 on 2019-04-14 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_group_portrait'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='info_id',
            new_name='recommend_info_id',
        ),
    ]
