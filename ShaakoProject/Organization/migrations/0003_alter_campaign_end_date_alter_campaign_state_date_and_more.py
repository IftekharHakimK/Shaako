# Generated by Django 4.0.2 on 2022-07-14 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0002_rename_compaign_details_campaign_campaign_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='state_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='upload_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='notification',
            name='timestamp',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='patientcampaign',
            name='enrollment_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='upload_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='visitform',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
