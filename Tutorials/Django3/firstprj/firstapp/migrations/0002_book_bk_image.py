# Generated by Django 3.0 on 2021-08-27 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bk_image',
            field=models.ImageField(default='default.jpg', upload_to='bookimage/'),
        ),
    ]