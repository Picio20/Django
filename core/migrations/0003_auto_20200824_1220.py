# Generated by Django 3.1 on 2020-08-24 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200824_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.IntegerField(choices=[(2, 'Conter-Strike'), (1, 'World of Warcraft'), (0, 'Unknown'), (3, 'League of Legends')], default=0),
        ),
    ]
