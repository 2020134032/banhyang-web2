# Generated by Django 3.0.4 on 2023-02-09 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0005_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songdata',
            name='bass',
        ),
        migrations.RemoveField(
            model_name='songdata',
            name='drum',
        ),
        migrations.RemoveField(
            model_name='songdata',
            name='guitar1',
        ),
        migrations.RemoveField(
            model_name='songdata',
            name='guitar2',
        ),
        migrations.RemoveField(
            model_name='songdata',
            name='keyboard1',
        ),
        migrations.RemoveField(
            model_name='songdata',
            name='keyboard2',
        ),
        migrations.RemoveField(
            model_name='songdata',
            name='vocal1',
        ),
        migrations.RemoveField(
            model_name='songdata',
            name='vocal2',
        ),
    ]