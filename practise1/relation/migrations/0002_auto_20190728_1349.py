# Generated by Django 2.2.2 on 2019-07-28 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antecedents', models.CharField(default='ANTECEDENTS', max_length=200)),
                ('consequents', models.CharField(default='CONSEQUENTS', max_length=200)),
                ('antecedent_support', models.CharField(default='ANTECEDENT_SUPPORT', max_length=200)),
                ('consequent_support', models.CharField(default='CONSEQUENT_SUPPORT', max_length=200)),
                ('support', models.CharField(default='SUPPORT', max_length=200)),
                ('confidence', models.CharField(default='CONFIDENCE', max_length=200)),
                ('lift', models.CharField(default='LIFT', max_length=200)),
                ('leverage', models.CharField(default='LEVERAGE', max_length=200)),
                ('conviction', models.CharField(default='CONVICTION', max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Association',
        ),
    ]
