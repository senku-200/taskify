# Generated by Django 5.0.6 on 2024-05-19 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_tasks_completestatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profession',
        ),
        migrations.AlterField(
            model_name='user',
            name='profilePhoto',
            field=models.ImageField(blank=True, null=True, upload_to='userProfilePhoto'),
        ),
    ]
