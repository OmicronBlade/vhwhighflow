# Generated by Django 3.2.6 on 2021-08-13 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vhwhighflow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='highflow',
            name='Ward',
            field=models.CharField(blank=True, choices=[('C1', 'C1'), ('C2', 'C2'), ('SSU', 'Short Stay Unit'), ('SMM', 'SMM'), ('SMF', 'SMF'), ('EC', 'Emergency Centre')], default='C2', max_length=3),
        ),
    ]
