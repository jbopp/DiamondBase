# Generated by Django 3.0.2 on 2020-02-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_database', '0008_auto_20200203_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='param',
            name='default_value',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='param',
            name='max_value',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='param',
            name='min_value',
            field=models.FloatField(null=True),
        ),
    ]