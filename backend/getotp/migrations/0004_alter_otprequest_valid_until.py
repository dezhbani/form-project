# Generated by Django 4.0.2 on 2022-02-08 11:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('getotp', '0003_alter_otprequest_valid_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otprequest',
            name='valid_until',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 8, 11, 30, 26, 38345, tzinfo=utc)),
        ),
    ]
