import os
from django.conf import settings
import json
from webstat.models import Users, Chat, Messages
from datetime import datetime
from django.db import transaction



def uploaddb(filename):
    path_to_file = os.path.join(settings.BASE_DIR, 'files', filename)
    with open(path_to_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with transaction.atomic():
        for message in data['messages']:
            chat, _ = Chat.objects.get_or_create(
                chat_id=data.get('id', None),
                name_chat=data.get('name', None),
                date_load=datetime.now()
            )

            from_id = None
            if message.get('from_id') is not None:
                if message['from_id'].startswith('user'):
                    from_id = int(message['from_id'][4:])
                else:
                    from_id = int(message['from_id'][7:])

            user, _ = Users.objects.get_or_create(
                name=message.get('from', None),
                from_id=from_id,
                chat_id=message.get('chat_id', None)
            )

            message_type = message.get('type', None)
            if message_type in ['message', 'channel_message']:
                Messages.objects.create(
                    date=datetime.strptime(message.get('date'), '%Y-%m-%dT%H:%M:%S'),
                    chat_id=chat,
                    text=message.get('text', ''),
                    stiker=message.get('stiker_emoji', None),
                    from_id=user,
                    file=message.get('file', None),
                )











