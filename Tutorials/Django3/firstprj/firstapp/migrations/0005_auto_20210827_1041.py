# Generated by Django 3.0 on 2021-08-27 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20210827_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bk_image',
            field=models.ImageField(default='default.jpg', upload_to='bk_image/'),
        ),
    ]