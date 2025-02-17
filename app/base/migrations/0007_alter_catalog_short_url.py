# Generated by Django 5.1.2 on 2024-12-20 08:49

import utils.helper
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_catalog_short_url_delete_catalogurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='short_url',
            field=models.URLField(default=utils.helper.generateShortUrl, max_length=300),
        ),
    ]
