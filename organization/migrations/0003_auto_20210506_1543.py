# Generated by Django 3.2 on 2021-05-06 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_alter_applicants_aplicants_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicants',
            name='applicants_kaps_issue',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='applicants',
            name='applicants_marketing_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='applicants',
            name='applicants_security_approved',
            field=models.BooleanField(default=False),
        ),
    ]