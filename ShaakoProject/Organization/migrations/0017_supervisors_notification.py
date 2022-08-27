# Generated by Django 4.0.2 on 2022-08-27 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0016_alter_patient_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supervisors_Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('description', models.CharField(max_length=100)),
                ('notification_type', models.CharField(max_length=100)),
                ('type_id', models.IntegerField()),
                ('is_read', models.BooleanField(default=False)),
                ('supervisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Organization.supervisor')),
            ],
        ),
    ]
