# Generated by Django 3.0.6 on 2020-06-04 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity_donat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='pick_up_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='pick_up_time',
            field=models.DateTimeField(null=True),
        ),
    ]
