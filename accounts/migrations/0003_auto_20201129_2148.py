# Generated by Django 3.1.3 on 2020-11-30 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201129_2137'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='siteuser',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='siteuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
