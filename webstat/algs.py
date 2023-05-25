import os
from django.conf import settings
import json
from webstat.models import Users, Chat, Messages
from datetime import datetime
from django.db import transaction
from collections import Counter
import re
from collections import defaultdict
from django.utils.timezone import make_aware


def uploaddb(filename):
    path_to_file = os.path.join(settings.BASE_DIR, 'files', filename)
    with open(path_to_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with transaction.atomic():
        for message in data['messages']:
            date_str = message.get("date")
            date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")

            chat, _ = Chat.objects.get_or_create(
                chat_id=data.get('id', None),
                name_chat=data.get('name', None),
                date_load=make_aware(date)
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
                    date=make_aware(date),
                    chat_id=chat,
                    text=message.get('text', ''),
                    stiker=message.get('stiker_emoji', None),
                    from_id=user,
                    file=message.get('file', None),
                )


def get_longest_message(filename):
    path_to_file = os.path.join(settings.BASE_DIR, 'files', filename)
    with open(path_to_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    messages = data.get("messages", [])
    user_messages = {}

    for message in messages:
        if not isinstance(message, dict):
            continue  # Пропуск сообщений, не являющихся словарями

        user = message.get('from')
        text = message.get('text', '')
        length = len(text)

        # Игнорирование сообщений без текста или без указанного отправителя
        if not text or not user:
            continue

        # Сохранение самого длинного сообщения пользователя
        if user not in user_messages:
            user_messages[user] = {'longest_message': text, 'message_length': length, 'fields': set()}
        else:
            if length > user_messages[user]['message_length']:
                user_messages[user]['longest_message'] = text
                user_messages[user]['message_length'] = length

        # Получение всех возможных полей и их типов из сообщений
        for key, value in message.items():
            if key in ['from', 'text']:  # Игнорирование известных полей
                continue
            user_messages[user]['fields'].add((key, type(value)))

    # Сортировка пользователей по длине их самых длинных сообщений
    sorted_users = sorted(user_messages.items(), key=lambda x: x[1]['message_length'], reverse=True)

    # Вывод самых длинных сообщений для 10 пользователей с нумерацией
    result = []
    for i, (user, message_info) in enumerate(sorted_users[:10], start=1):
        formatted_string = f"{i}. {user}: {message_info['longest_message']} (длина сообщения: {message_info['message_length']})"
        result.append(formatted_string)

    return result




def get_top_words(filename,top_n):
    path_to_file = os.path.join(settings.BASE_DIR, 'files', filename)
    with open(path_to_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    messages = data.get("messages", [])
    all_words = []

    for message in messages:
        if isinstance(message, dict) and 'text' in message:
            text = message['text']
            if isinstance(text, str):  # Проверка, что 'text' является строкой
                words = re.findall(r'\b\w+\b', text.lower())  # Извлечение всех слов из текста сообщения
                all_words.extend(words)

    word_counts = Counter(all_words)
    top_words = word_counts.most_common(top_n)

    result = []
    for i, (word, count) in enumerate(top_words, start=1):
        formatted_string = f"{i}. Word: {word}, Count: {count}"
        result += "\n"
        result.append(formatted_string)

    return result
def get_top_active_users(filename,top_n):
    path_to_file = os.path.join(settings.BASE_DIR, 'files', filename)
    with open(path_to_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    messages = data.get("messages", [])
    user_message_counts = defaultdict(int)

    for message in messages:
        if isinstance(message, dict) and 'from' in message:
            user = message['from']
            if user in user_message_counts:
                user_message_counts[user] += 1
            else:
                user_message_counts[user] = 1

    sorted_users = sorted(user_message_counts.items(), key=lambda x: x[1], reverse=True)
    formatted_output = []
    for i, (user, count) in enumerate(sorted_users[:top_n], start=1):
        formatted_output.append(f"{i}. Пользователь: {user}, Количество сообщений: {count}")

    return formatted_output



def get_chatid(filename):
    path_to_file = os.path.join(settings.BASE_DIR, 'files', filename)
    with open(path_to_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get('name',None)

def get_chatname(filename):
    path_to_file = os.path.join(settings.BASE_DIR, 'files', filename)
    with open(path_to_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get('id',None)












