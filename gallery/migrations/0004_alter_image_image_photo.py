# Generated by Django 4.0.4 on 2022-05-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_alter_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_photo',
            field=models.ImageField(default='media/articles/car3', null=True, upload_to='galleries'),
        ),
    ]