# Generated by Django 4.2.5 on 2023-11-03 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_attos', '0003_quantidadedoadores'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotos',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='instagramprofile',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='quantidadedoadores',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
