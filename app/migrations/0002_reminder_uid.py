# Generated by Django 3.1.5 on 2021-01-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='uid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
