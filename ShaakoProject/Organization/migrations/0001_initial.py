# Generated by Django 4.0.2 on 2022-07-14 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('state_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(auto_now_add=True)),
                ('compaign_details', models.CharField(max_length=300)),
                ('goal', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CHW',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contactNo', models.CharField(max_length=100)),
                ('presentAddress', models.CharField(max_length=100)),
                ('imagePath', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=2000)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('upazilla_thana', models.CharField(max_length=100)),
                ('ward_union', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=100)),
                ('notification_type', models.CharField(max_length=100)),
                ('type_id', models.CharField(max_length=100)),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('officeAddress', models.CharField(max_length=100)),
                ('contactNo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('contactNo', models.CharField(max_length=100)),
                ('date_of_birth', models.DateTimeField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('relatedLesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='QuizItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('option_1', models.CharField(max_length=100)),
                ('option_2', models.CharField(max_length=100)),
                ('option_3', models.CharField(max_length=100)),
                ('option_4', models.CharField(max_length=100)),
                ('point', models.IntegerField()),
                ('correct_option', models.IntegerField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='QuizSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('chw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.chw')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contactNo', models.CharField(max_length=100)),
                ('presentAddress', models.CharField(max_length=100)),
                ('imagePath', models.CharField(max_length=100)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.organization')),
            ],
        ),
        migrations.CreateModel(
            name='VisitForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('temperature', models.FloatField()),
                ('blood_pressure', models.FloatField()),
                ('headache_level', models.IntegerField()),
                ('nausea_level', models.IntegerField()),
                ('insomniac_level', models.IntegerField()),
                ('dyspnoea_level', models.IntegerField()),
                ('cough_level', models.IntegerField()),
                ('other_problems', models.CharField(max_length=200)),
                ('assumed_disease', models.CharField(max_length=100)),
                ('suggestions', models.CharField(max_length=200)),
                ('summary_impression', models.CharField(max_length=200)),
                ('next_visit_date', models.DateTimeField()),
                ('chw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.chw')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor_Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.campaign')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.supervisor')),
            ],
        ),
        migrations.CreateModel(
            name='SubmissionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chosenOption', models.IntegerField()),
                ('quizItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.quizitem')),
                ('quizSubmission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.quizsubmission')),
            ],
        ),
        migrations.CreateModel(
            name='PatientCampaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateTimeField(auto_now_add=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.campaign')),
                ('chw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.chw')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.patient')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contactNo', models.CharField(max_length=100)),
                ('presentAddress', models.CharField(max_length=100)),
                ('imagePath', models.CharField(max_length=100)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Location_Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.campaign')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.location')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson_CHW',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_read', models.BooleanField(default=False)),
                ('dateOfRead', models.DateTimeField()),
                ('chw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.chw')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.lesson')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='supervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.supervisor'),
        ),
        migrations.AddField(
            model_name='chw',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.location'),
        ),
        migrations.AddField(
            model_name='chw',
            name='supervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organization.supervisor'),
        ),
    ]
