# Generated by Django 5.2 on 2025-04-05 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ckd_app', '0002_remove_ckdrecord_smoking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ckdrecord',
            name='wc',
            field=models.IntegerField(),
        ),
    ]
