# Generated by Django 2.1 on 2019-10-03 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='designcategory',
            name='featured_image',
            field=models.ImageField(null=True, upload_to='images/%Y/%m/%d'),
        ),
    ]
