# Generated by Django 4.0.4 on 2022-05-21 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppHoppiness', '0002_comida_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='comida',
            name='precio_happy_hour',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='comida',
            name='precio_regular',
            field=models.FloatField(default=0.0),
        ),
    ]
