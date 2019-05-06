# Generated by Django 2.2 on 2019-05-01 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_recordrecommend'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('file_id', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(blank=True, max_length=100)),
                ('file', models.ImageField(upload_to='%Y/%m/%d/')),
            ],
        ),
        migrations.AlterField(
            model_name='recordrecommend',
            name='record_recommend',
            field=models.TextField(blank=True),
        ),
    ]
