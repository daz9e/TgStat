import os
from django.conf import settings
import json
from webstat.models import User

def addusers(filename):
    path_to_file = os.path.join(settings.BASE_DIR, 'files', filename)
    with open(path_to_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        messages = data["messages"]
        print("handle messages!")
    for message in messages:
        try:
            id = message.get("from_id", "")[4:]
            name = message.get("from", "")
            user, created = User.objects.get_or_create(user_id=id, username=name)
            if created:
                print(f"New user created: {name} ({id})")
        except Exception as e:
            print(f"Error creating user: {e}")
            continue



