# Generated by Django 4.2.1 on 2023-05-10 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webstat', '0003_chat_users_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='chat_id',
            field=models.IntegerField(null=True),
        ),
    ]
