# Generated by Django 2.0.2 on 2018-03-06 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20180306_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipe',
            name='tipo_cargo',
            field=models.CharField(choices=[(1, 'Doscente'), (2, 'Discente')], max_length=20),
        ),
    ]