# Generated by Django 4.1.7 on 2024-02-27 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
