# Generated by Django 4.2.3 on 2023-07-31 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pokemon', '0002_rename_pokemon_pokemondata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemondata',
            old_name='hight',
            new_name='height',
        ),
    ]
