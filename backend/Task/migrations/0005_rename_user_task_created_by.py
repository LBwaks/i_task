# Generated by Django 5.1.3 on 2025-03-19 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0004_task_user_alter_task_assigned_to'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='user',
            new_name='created_by',
        ),
    ]
