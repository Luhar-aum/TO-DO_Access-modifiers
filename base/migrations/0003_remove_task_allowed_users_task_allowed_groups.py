# Generated by Django 5.2 on 2025-05-07 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('base', '0002_task_allowed_users_task_visibility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='allowed_users',
        ),
        migrations.AddField(
            model_name='task',
            name='allowed_groups',
            field=models.ManyToManyField(blank=True, to='auth.group'),
        ),
    ]
