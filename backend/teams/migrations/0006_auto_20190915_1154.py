# Generated by Django 2.2.5 on 2019-09-15 06:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_student_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github_url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='students',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
