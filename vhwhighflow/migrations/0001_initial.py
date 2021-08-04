# Generated by Django 3.2.6 on 2021-08-04 20:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='highflow',
            fields=[
                ('FolderNo', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Folder No')),
                ('Name', models.CharField(max_length=50)),
                ('Age', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(75)])),
                ('Background', models.TextField(blank=True, max_length=255)),
                ('PriorityScore', models.PositiveIntegerField(default=1, verbose_name='Priority Score')),
                ('PriorityScoreDate', models.DateField(verbose_name='Priority Score Date')),
                ('UpdatedPriority', models.PositiveIntegerField(blank=True, null=True, verbose_name='Updated Priority Score')),
                ('UpdatedPriorityDate', models.DateField(blank=True, null=True, verbose_name='Updated Date')),
                ('HFStart', models.DateField(verbose_name='Date Starting High Flow')),
                ('Archive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='sats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField()),
                ('RespRate', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(60)], verbose_name='Resp Rate')),
                ('HeartRate', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(40), django.core.validators.MaxValueValidator(200)], verbose_name='Heart Rate')),
                ('Sats', models.PositiveIntegerField(default=90, validators=[django.core.validators.MinValueValidator(40), django.core.validators.MaxValueValidator(100)])),
                ('FiO2', models.PositiveIntegerField(default=21, validators=[django.core.validators.MinValueValidator(21), django.core.validators.MaxValueValidator(100)])),
                ('Litres', models.PositiveIntegerField(default=10, validators=[django.core.validators.MinValueValidator(25), django.core.validators.MaxValueValidator(60)])),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vhwhighflow.highflow')),
            ],
        ),
    ]
