# Generated by Django 4.0 on 2022-05-01 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonapp', '0004_candidate_hogar_employee_candidate_person_name1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hr_form',
            name='interview_date',
            field=models.DateTimeField(default='2006-10-25', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hr_form',
            name='interviewers',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
