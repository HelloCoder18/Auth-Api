# Generated by Django 4.2.3 on 2023-08-03 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipes', '0002_alter_recipe_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
