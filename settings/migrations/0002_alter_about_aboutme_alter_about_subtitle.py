# Generated by Django 4.1.4 on 2023-01-04 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='aboutme',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='about',
            name='subtitle',
            field=models.TextField(max_length=10000),
        ),
    ]
