from core import *
from data_store import *

for event in core.longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        command = event.text.lower()
        user_id = str(event.user_id)
        msg = event.text.lower()
        if command == 'привет':
            core.write_msg(user_id, f'Привет, {core.name(user_id)}, чтобы начать поиск партнера отправь букву "П"')

        elif command == 'п':
            creating_database()
            core.write_msg(user_id, 'Идёт поиск...')
            core.find_user(user_id)
            core.write_msg(event.user_id, f'Найдено несколько совпадений, нажмите "С" для перехода к следующему человеку')
            core.find_persons(user_id, offset)

        elif command == 'с':
            for i in line:
                offset += 1
                core.find_persons(user_id, offset)
                break
        elif command == 'пока':
            core.write_msg(user_id, f'пока, {core.name(user_id)}')
        else:
            core.write_msg(event.user_id, 'Неверная команда. Введите "П" для поиска или "С" для перехода к следующему человеку')