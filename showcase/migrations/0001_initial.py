# Generated by Django 2.1 on 2019-10-02 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
                ('likes', models.IntegerField(null=True)),
                ('date_added', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DesignCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Design Categories',
            },
        ),
        migrations.AddField(
            model_name='design',
            name='design_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase.DesignCategory'),
        ),
    ]
