# Generated by Django 4.2 on 2023-05-06 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_foodproduct_ingredients_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodproduct',
            name='image',
            field=models.ImageField(default='static/food_products/default.png', upload_to='static/food_products/'),
        ),
    ]
