# Generated by Django 3.2 on 2021-05-06 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_alter_applicants_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicants',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]