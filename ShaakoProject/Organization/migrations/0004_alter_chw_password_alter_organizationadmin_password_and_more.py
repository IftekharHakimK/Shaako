# Generated by Django 4.0.2 on 2022-07-15 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0003_alter_campaign_end_date_alter_campaign_state_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chw',
            name='password',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='organizationadmin',
            name='password',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='password',
            field=models.CharField(max_length=512),
        ),
    ]
