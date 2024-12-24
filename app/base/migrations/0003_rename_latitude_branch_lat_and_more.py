# Generated by Django 5.1.2 on 2024-12-01 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_serviceoffer_organizations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='latitude',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='branch',
            old_name='longitude',
            new_name='long',
        ),
        migrations.AddField(
            model_name='organization',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='long',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='branch',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
