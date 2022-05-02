# Generated by Django 4.0 on 2022-02-22 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonapp', '0002_alter_candidate_entry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hr_form',
            name='interviewed',
            field=models.BooleanField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='hr_form',
            name='medicalval',
            field=models.BooleanField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='hr_form',
            name='observaciones1',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='hr_form',
            name='observaciones2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='hr_form',
            name='observaciones3',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='hr_form',
            name='observaciones4',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='hr_form',
            name='psychometric',
            field=models.BooleanField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='hr_form',
            name='result1',
            field=models.BooleanField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='hr_form',
            name='result2',
            field=models.BooleanField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='hr_form',
            name='result3',
            field=models.BooleanField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='hr_form',
            name='result4',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='hr_form',
            name='terapy',
            field=models.BooleanField(blank=True, max_length=40, null=True),
        ),
    ]
