# Generated by Django 2.1.7 on 2019-03-29 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190219_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='userConcern',
            field=models.CharField(choices=[('emergency', 'EMERGENCY')], default='emergency', max_length=9),
        ),
    ]
