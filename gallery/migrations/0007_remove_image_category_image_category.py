# Generated by Django 4.0.4 on 2022-05-29 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_alter_image_image_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ManyToManyField(to='gallery.category'),
        ),
    ]
