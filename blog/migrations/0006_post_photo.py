# Generated by Django 3.1.1 on 2020-09-10 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default=None, upload_to='photos'),
        ),
    ]
