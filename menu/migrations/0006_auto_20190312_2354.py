# Generated by Django 2.1.7 on 2019-03-12 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20190312_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='grower',
            name='order',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='origin',
            name='order',
            field=models.IntegerField(default=-1),
        ),
    ]