# Generated by Django 2.1.7 on 2019-03-29 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190328_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthCareLocations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]