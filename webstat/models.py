from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=True)
    from_id = models.IntegerField(null=True)
    chat_id = models.IntegerField(null=True)

class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    chat_id = models.IntegerField(null=True)
    name_chat = models.CharField(max_length=100,null=True)
    date_load = models.DateTimeField(null=True )

class Messages(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(null=True)
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE,null=True)
    text = models.TextField()
    stiker = models.CharField(max_length=100,null=True)
    from_id = models.ForeignKey(Users, on_delete=models.CASCADE,null=True)
    file = models.FileField(null=True)
    forwarded_from = models.ForeignKey('self', on_delete=models.CASCADE, related_name='forwarded_messages', null=True, blank=True)
    saved_from = models.ForeignKey('self', on_delete=models.CASCADE, related_name='saved_messages', null=True, blank=True)
    reply_to_message_id = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply_messages', null=True, blank=True)


