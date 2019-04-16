# Generated by Django 2.1.7 on 2019-04-09 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190409_0630'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('collection_id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='recommendedinfo',
            name='info_name',
            field=models.CharField(default='jintiantianqibucuo', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='info_id',
            field=models.ManyToManyField(blank=True, to='api.RecommendedInfo'),
        ),
    ]