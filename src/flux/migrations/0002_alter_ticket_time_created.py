# Generated by Django 3.2.9 on 2021-12-27 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flux', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
