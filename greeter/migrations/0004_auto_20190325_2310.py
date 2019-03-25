# Generated by Django 2.1.7 on 2019-03-25 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greeter', '0003_auto_20190321_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='musician',
            name='instrument',
            field=models.CharField(choices=[('guitar', 'Guitar'), ('bass', 'Bass'), ('drums', 'Drums'), ('vocals', 'Vocals'), ('brass', 'Brass'), ('piano', 'Piano'), ('harmonica', 'Harmonica')], max_length=255),
        ),
    ]
