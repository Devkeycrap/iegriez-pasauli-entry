# Generated by Django 3.2.3 on 2021-05-31 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_alter_mapicon_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapicon',
            name='image',
            field=models.ImageField(upload_to='core/images'),
        ),
    ]
