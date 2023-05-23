# Generated by Django 4.2.1 on 2023-05-05 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('language_code', models.CharField(max_length=10)),
                ('is_bot', models.BooleanField()),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('edited', models.CharField(max_length=10)),
                ('text_entities', models.JSONField()),
                ('performer', models.CharField(max_length=100)),
                ('thumbnail', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('mime_type', models.CharField(max_length=100)),
                ('file', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('via_bot', models.CharField(max_length=100)),
                ('date_unixtime', models.CharField(max_length=100)),
                ('reply_to_message_id', models.IntegerField()),
                ('photo', models.CharField(max_length=100)),
                ('sticker_emoji', models.CharField(max_length=100)),
                ('duration_seconds', models.IntegerField()),
                ('members', models.JSONField()),
                ('action', models.CharField(max_length=100)),
                ('width', models.IntegerField()),
                ('actor', models.CharField(max_length=100)),
                ('media_type', models.CharField(max_length=100)),
                ('height', models.IntegerField()),
                ('edited_unixtime', models.CharField(max_length=100)),
                ('from_id', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('forwarded_from', models.CharField(max_length=100)),
                ('actor_id', models.CharField(max_length=100)),
                ('saved_from', models.CharField(max_length=100)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webstat.user')),
            ],
        ),
    ]
