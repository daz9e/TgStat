# Generated by Django 4.2.1 on 2023-05-15 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webstat', '0010_alter_users_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='forwarded_from',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='reply_to_message_id',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='saved_from',
        ),
    ]