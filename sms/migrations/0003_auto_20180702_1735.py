# Generated by Django 2.0 on 2018-07-02 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_auto_20180702_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='apikey',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='secure_hash',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
