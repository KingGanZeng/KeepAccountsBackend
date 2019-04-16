# Generated by Django 2.1.7 on 2019-04-15 09:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_group_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wish',
            old_name='wish_type',
            new_name='wish_first_category',
        ),
        migrations.AddField(
            model_name='wish',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='wish',
            name='wish_second_category',
            field=models.CharField(default='娱乐', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wish',
            name='create_timestamp',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wish',
            name='update_timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]