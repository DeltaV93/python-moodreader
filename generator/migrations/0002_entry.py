# Generated by Django 2.1.5 on 2019-01-19 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.CharField(max_length=1000)),
                ('gradient_color_stop_1', models.CharField(max_length=25)),
                ('gradient_color_stop_2', models.CharField(max_length=25)),
                ('gradient_color_stop_3', models.CharField(max_length=25)),
            ],
        ),
    ]