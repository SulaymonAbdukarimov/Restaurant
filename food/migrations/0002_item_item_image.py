# Generated by Django 3.2.4 on 2021-06-23 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://cdn.dribbble.com/users/1012566/screenshots/4187820/topic-2.jpg', max_length=500),
        ),
    ]
