# Generated by Django 4.2.5 on 2023-09-29 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_band_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
