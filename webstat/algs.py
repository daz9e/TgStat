import os
from django.conf import settings
import json
from webstat.models import User

def addusers(filename):
    path_to_file = os.path.join(settings.BASE_DIR, 'files', filename)
    with open(path_to_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        messages = data["messages"]
    for message in messages:
        try:
            id = message["from_id"][4:]
            name = message["from"]
            user = User(user_id=id, username=name)
            user.save()
        except:
            continue


