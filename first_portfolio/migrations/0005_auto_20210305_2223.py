# Generated by Django 3.1.7 on 2021-03-05 22:23

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('first_portfolio', '0004_work_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='image',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='img/upload'),
        ),
    ]
