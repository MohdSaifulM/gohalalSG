# Generated by Django 3.1.4 on 2020-12-17 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20201216_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='lng',
            field=models.FloatField(null=True),
        ),
    ]