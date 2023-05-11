import os
from django.conf import settings
import json
from webstat.models import Users, Chat, Messages
from datetime import datetime




def uploaddb(filename):
    path_to_file = os.path.join(settings.BASE_DIR, 'files', filename)
    with open(path_to_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for message in data['messages']:
        chat, _ = Chat.objects.get_or_create(
            chat_id=data.get('id', None),
            name_chat=data.get('name'),
            date_load=datetime.now()
        )
        if message.get('from_id') is None:
            from_id_user = None
        elif message.get('from_id').startswith('user'):
            from_id_user = int(message.get('from_id')[4:])
        else:
            from_id_user = int(message.get('from_id')[7:])

        user, _ = Users.objects.get_or_create(
            name=message.get('from', None),
            from_id=from_id_user,
        )

        forwarded_from_id = message.get('forwarded_from', None)
        if forwarded_from_id is not None:
            forwarded_from = Messages.objects.get(forwarded_from_id=forwarded_from_id)
        else:
            forwarded_from = None

        message_type = message.get('type', None)
        if message_type == 'message':
            Messages.objects.create(
                date=datetime.strptime(message.get('date'), '%Y-%m-%dT%H:%M:%S'),
                chat_id=chat,
                text=message.get('text', None),
                stiker=message.get('stiker_emoji', None),
                from_id=message.get('from_id'),
                file=message.get('file', None),
                forwarded_from=forwarded_from,
                saved_from=message.get('saved_from', None),
                reply_to_message_id=message.get('reply_to_message_id', None)
            )
        elif message_type == 'channel_message':
            Messages.objects.create(
                id=message.get('id', None),
                date=datetime.strptime(message.get('date'), '%Y-%m-%dT%H:%M:%S'),
                chat_id=chat,
                text=message.get('text', None),
                stiker=message.get('stiker_emoji', None),
                from_id=message.get('from_id'),
                file=message.get('file', None),
                forwarded_from=forwarded_from,
                saved_from=message.get('saved_from', None),
                reply_to_message_id=message.get('reply_to_message_id', None)
            )









