import os
from django.conf import settings
import json

from collections import defaultdict
from webstat.models import Users, Chat, Messages
from datetime import datetime




def uploaddb(filename):
    path_to_file = os.path.join(settings.BASE_DIR, 'files', filename)
    with open(path_to_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for message in data['messages']:
        chat, _ = Chat.objects.get_or_create(
            chat_id=data.get('id', None),
            name_chat=data.get('name', None),
            date_load=datetime.now()
        )
        if message.get('from_id') is None:
            from_id_user = None
        else:
            from_id_user = int(message.get('from_id')[-10:])

        user, _ = Users.objects.get_or_create(
            name=message.get('from', None),
            from_id = from_id_user
        )

        Messages.objects.create(
            date=datetime.strptime(message.get('date'), '%Y-%m-%dT%H:%M:%S'),
            chat_id=chat,
            text=message.get('text', None),
            stiker=message.get('stiker', None),
            from_id=user,
            file=message.get('file', None),
            forwarded_from=message.get('forwarded_from', None),
            saved_from=message.get('saved_from', None),
            reply_to_message_id=message.get('reply_to_message_id', None)

        )





