# Generated by Django 2.2.2 on 2019-06-19 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='summary',
        ),
        migrations.AddField(
            model_name='product',
            name='cosmetics',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='groceries',
            field=models.CharField(max_length=200, null=True),
        ),
    ]