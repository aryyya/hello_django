# Generated by Django 2.1.7 on 2019-03-13 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_auto_20190313_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='teaitem',
            name='tasting_notes',
            field=models.CharField(default='', max_length=64),
        ),
    ]