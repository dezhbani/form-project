# Generated by Django 4.0.2 on 2022-02-09 15:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('getotp', '0004_alter_otprequest_valid_until'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otprequest',
            name='valid_until',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 9, 15, 33, 39, 898787, tzinfo=utc)),
        ),
    ]
