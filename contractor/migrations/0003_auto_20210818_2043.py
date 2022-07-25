# Generated by Django 3.2.6 on 2021-08-18 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contractor', '0002_rename_labour_detail_contractor_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contractor_detail',
            old_name='labour_city',
            new_name='contractor_city',
        ),
        migrations.RenameField(
            model_name='contractor_detail',
            old_name='labour_dob',
            new_name='contractor_dob',
        ),
        migrations.RenameField(
            model_name='contractor_detail',
            old_name='labour_email',
            new_name='contractor_email',
        ),
        migrations.RenameField(
            model_name='contractor_detail',
            old_name='labour_specification',
            new_name='contractor_jobdetails',
        ),
        migrations.RenameField(
            model_name='contractor_detail',
            old_name='labour_name',
            new_name='contractor_name',
        ),
        migrations.RenameField(
            model_name='contractor_detail',
            old_name='labour_state',
            new_name='contractor_state',
        ),
    ]
