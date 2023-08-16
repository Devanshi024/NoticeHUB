# Generated by Django 4.1.5 on 2023-08-12 07:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0009_postmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='upload/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])]),
        ),
    ]