# Generated by Django 4.2.1 on 2023-05-10 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webstat', '0002_remove_user_date_joined_remove_user_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('chat_id', models.IntegerField()),
                ('name_chat', models.CharField(max_length=100)),
                ('date_load', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('from_id', models.IntegerField()),
                ('chat_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('text', models.TextField()),
                ('stiker', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='')),
                ('chat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstat.chat')),
                ('forwarded_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forwarded_messages', to='webstat.messages')),
                ('from_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstat.user')),
                ('reply_to_message_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_messages', to='webstat.messages')),
                ('saved_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saved_messages', to='webstat.messages')),
            ],
        ),
    ]