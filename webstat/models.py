from django.db import models

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)

class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    chat_id = models.IntegerField()
    name_chat = models.CharField(max_length=100)
    date_load = models.DateTimeField()

class Messages(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)
    text = models.TextField()
    stiker = models.CharField(max_length=100)
    from_id = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField()
    forwarded_from = models.ForeignKey('self', on_delete=models.CASCADE, related_name='forwarded_messages', null=True, blank=True)
    saved_from = models.ForeignKey('self', on_delete=models.CASCADE, related_name='saved_messages', null=True, blank=True)
    reply_to_message_id = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply_messages', null=True, blank=True)

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    from_id = models.IntegerField()
    chat_id = models.IntegerField()
