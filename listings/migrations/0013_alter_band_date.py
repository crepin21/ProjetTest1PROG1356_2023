# Generated by Django 4.2.5 on 2023-09-29 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0012_alter_band_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='date',
            field=models.DateField(),
        ),
    ]
