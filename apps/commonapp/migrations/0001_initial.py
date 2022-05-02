# Generated by Django 4.0 on 2022-02-21 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='HR_Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_num', models.IntegerField()),
                ('name', models.CharField(max_length=40)),
                ('interviewed', models.BooleanField(max_length=40)),
                ('result1', models.BooleanField(max_length=40)),
                ('observaciones1', models.CharField(max_length=250)),
                ('terapy', models.BooleanField(max_length=40)),
                ('result2', models.BooleanField(max_length=40)),
                ('observaciones2', models.CharField(max_length=250)),
                ('result3', models.BooleanField(max_length=40)),
                ('observaciones3', models.CharField(max_length=250)),
                ('medicalval', models.BooleanField(max_length=40)),
                ('psychometric', models.BooleanField(max_length=40)),
                ('result4', models.CharField(max_length=250)),
                ('observaciones4', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=40)),
                ('identification', models.CharField(max_length=40)),
                ('direction', models.CharField(max_length=250)),
                ('birth_date', models.DateTimeField(max_length=40)),
                ('candidate_phone', models.CharField(max_length=40)),
                ('mail', models.EmailField(max_length=40)),
                ('civil_status', models.CharField(max_length=40)),
                ('spouse', models.CharField(max_length=40)),
                ('children_option', models.BooleanField(max_length=40)),
                ('children_quantity', models.CharField(max_length=40)),
                ('dependency_quantity', models.CharField(max_length=40)),
                ('blood_type', models.CharField(max_length=40)),
                ('license_type', models.CharField(max_length=40)),
                ('vehicle_option', models.BooleanField(max_length=40)),
                ('profession', models.CharField(max_length=40)),
                ('salary', models.CharField(max_length=40)),
                ('date', models.DateTimeField(max_length=40)),
                ('studies', models.CharField(max_length=40)),
                ('illness_option', models.BooleanField(max_length=40)),
                ('illness', models.CharField(max_length=40)),
                ('company_name', models.CharField(max_length=40)),
                ('compnay_phone', models.CharField(max_length=40)),
                ('old_job', models.CharField(max_length=40)),
                ('final_salary', models.CharField(max_length=40)),
                ('entry_date', models.CharField(max_length=40)),
                ('departure_date', models.DateTimeField(max_length=40)),
                ('boss_name', models.CharField(max_length=40)),
                ('exit_reason', models.CharField(max_length=40)),
                ('family_option', models.BooleanField(max_length=40)),
                ('familiar', models.CharField(max_length=40)),
                ('photo', models.ImageField(upload_to='')),
                ('cv', models.FileField(upload_to='')),
                ('handling_option', models.BooleanField(max_length=40)),
                ('other_studies', models.CharField(max_length=250)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='commonapp.jobs')),
                ('nationality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='commonapp.country')),
            ],
        ),
    ]