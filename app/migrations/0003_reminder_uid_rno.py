# Generated by Django 3.1.5 on 2021-01-28 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_reminder_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='uid_rno',
            field=models.IntegerField(default=0),
        ),
    ]
