# Generated by Django 2.1.7 on 2019-04-13 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20190413_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='id',
        ),
        migrations.AddField(
            model_name='group',
            name='group_info_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
