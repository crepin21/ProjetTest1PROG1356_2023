# Generated by Django 4.2.5 on 2023-09-29 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0016_alter_band_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='pension',
            field=models.PositiveIntegerField(default=9945),
            preserve_default=False,
        ),
    ]
