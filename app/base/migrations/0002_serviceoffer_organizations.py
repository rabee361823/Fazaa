# Generated by Django 5.1.2 on 2024-11-29 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceoffer',
            name='organizations',
            field=models.ManyToManyField(to='base.organizationtype'),
        ),
    ]
