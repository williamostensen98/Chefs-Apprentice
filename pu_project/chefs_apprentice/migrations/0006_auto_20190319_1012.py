# Generated by Django 2.1.7 on 2019-03-19 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chefs_apprentice', '0005_recipe_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='food_pics/default.jpg', upload_to='food_pics'),
        ),
    ]
