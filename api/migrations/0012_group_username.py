# Generated by Django 2.1.7 on 2019-04-14 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20190414_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='username',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
