# Generated by Django 4.2 on 2023-04-15 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_foodproduct_ingredients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodproduct',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='foodproduct',
            name='ingredients',
            field=models.ManyToManyField(to='main.ingredients'),
        ),
    ]
