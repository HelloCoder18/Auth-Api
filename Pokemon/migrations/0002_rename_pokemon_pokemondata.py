# Generated by Django 4.2.3 on 2023-07-31 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pokemon', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pokemon',
            new_name='Pokemondata',
        ),
    ]