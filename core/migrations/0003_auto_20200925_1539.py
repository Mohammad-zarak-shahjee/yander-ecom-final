# Generated by Django 3.0.8 on 2020-09-25 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200925_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='email',
        ),
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
