# Generated by Django 2.1.7 on 2019-03-21 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('greeter', '0002_pizza_toppings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('genre', models.CharField(choices=[('rock', 'Rock'), ('hip-hop', 'Hip Hop'), ('jazz', 'Jazz')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='greeter.Band')),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('instrument', models.CharField(choices=[('guitar', 'Guitar'), ('bass', 'Bass'), ('drums', 'Drums'), ('vocals', 'Vocals'), ('brass', 'Brass'), ('piano', 'Piano')], max_length=255)),
                ('band', models.ManyToManyField(through='greeter.Member', to='greeter.Band')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='musician',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='greeter.Musician'),
        ),
    ]