# Generated by Django 2.1.7 on 2019-03-15 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teaitem',
            name='price_bowl',
            field=models.CharField(blank=True, default='', max_length=16),
        ),
    ]