# Generated by Django 5.2 on 2025-04-04 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CKDRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.FloatField()),
                ('bp', models.FloatField()),
                ('sg', models.FloatField()),
                ('al', models.FloatField()),
                ('su', models.FloatField()),
                ('rbc', models.FloatField()),
                ('pc', models.FloatField()),
                ('pcc', models.FloatField()),
                ('ba', models.FloatField()),
                ('bgr', models.FloatField()),
                ('bu', models.FloatField()),
                ('sc', models.FloatField()),
                ('sod', models.FloatField()),
                ('pot', models.FloatField()),
                ('hemo', models.FloatField()),
                ('pcv', models.FloatField()),
                ('wc', models.FloatField()),
                ('rc', models.FloatField()),
                ('htn', models.CharField(max_length=10)),
                ('dm', models.CharField(max_length=10)),
                ('cad', models.CharField(max_length=10)),
                ('appet', models.CharField(max_length=10)),
                ('pe', models.CharField(max_length=10)),
                ('ane', models.CharField(max_length=10)),
                ('sex', models.CharField(max_length=10)),
                ('smoking', models.CharField(max_length=10)),
                ('result', models.CharField(max_length=100)),
                ('predicted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
