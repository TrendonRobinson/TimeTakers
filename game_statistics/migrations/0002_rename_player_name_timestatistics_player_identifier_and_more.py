# Generated by Django 4.2.3 on 2023-07-25 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game_statistics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timestatistics',
            old_name='player_name',
            new_name='player_identifier',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='player_name',
        ),
    ]
