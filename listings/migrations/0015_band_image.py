# Generated by Django 4.2.5 on 2023-09-29 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0014_band_admis_alter_band_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
