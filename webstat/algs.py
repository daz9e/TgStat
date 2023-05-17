import os
from django.conf import settings
import json
from webstat.models import Users, Chat, Messages
from datetime import datetime
from django.db import transaction
from collections import Counter
import re


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
    print("Список пользователей с самыми длинными сообщениями:")
    for i, (user, message_info) in enumerate(sorted_users[:10], start=1):
        print(f"{i}. {user}: {message_info['longest_message']} (длина сообщения: {message_info['message_length']})")
        print(' ')
    return user_messages




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

    print(f"Топ {top_n} наиболее часто встречающихся слов:")
    for i, (word, count) in enumerate(top_words, start=1):
        print(f"{i}. Слово: {word}, Количество: {count}")














