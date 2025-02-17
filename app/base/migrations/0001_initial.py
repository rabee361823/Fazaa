# Generated by Django 5.1.2 on 2024-11-29 15:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('icon', models.ImageField(default='about_us/default_about_us.png', upload_to='media/about_us/')),
            ],
        ),
        migrations.CreateModel(
            name='CommonQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.ImageField(default='delivery_company/default_company.png', upload_to='media/delivery_company/')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commercial_register_id', models.IntegerField()),
                ('logo', models.ImageField(default='organizations/logos/default.png', upload_to='media/organizations/logos/')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('website', models.CharField(blank=True, max_length=300, null=True)),
                ('website_short_link', models.CharField(blank=True, max_length=30, null=True)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.ImageField(default='social_media/default_media.png', upload_to='media/social_media/')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('template', models.ImageField(upload_to='media/templates/')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/image_galleries/')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.organization')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryCompanyLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_link', models.URLField(max_length=300)),
                ('short_link', models.URLField(max_length=30)),
                ('active', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('delivery_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.deliverycompany')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalog_type', models.CharField(choices=[('MENU', 'Menu'), ('DISCOUNT', 'Discount'), ('OFFERS', 'Offers')], max_length=255)),
                ('file', models.FileField(upload_to='media/catalogs/')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('description', models.CharField(max_length=255)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.organization')),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='organization_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.organizationtype'),
        ),
        migrations.CreateModel(
            name='ReelsGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='media/reels_galleries/')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.organization')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('expiresAt', models.DateField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.organization')),
            ],
        ),
        migrations.CreateModel(
            name='SocialMediaLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_link', models.URLField(max_length=300)),
                ('short_link', models.URLField(max_length=30)),
                ('active', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.organization')),
                ('social_media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.socialmedia')),
            ],
        ),
        migrations.CreateModel(
            name='ClientOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('expiresAt', models.DateField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.organization')),
                ('template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.template')),
            ],
        ),
    ]
