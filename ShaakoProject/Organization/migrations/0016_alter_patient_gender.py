# Generated by Django 4.0.2 on 2022-08-27 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0015_alter_visitform_blood_pressure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(max_length=20),
        ),
    ]
