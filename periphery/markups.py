from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button_menu = InlineKeyboardButton("Меню", callback_data="menu")

def lessons_list(lessons):
    keyboard = InlineKeyboardMarkup(row_width=1)
    for lesson in lessons:
        button = InlineKeyboardButton(lesson.name, callback_data=f"lesson/{lesson.Id}")
        keyboard.add(button)
        
    return keyboard


def lesson_enter(lesson_id):
    keyboard = InlineKeyboardMarkup(row_width=2)
    button_enter = InlineKeyboardButton("Вступить", callback_data=f"enter/{lesson_id}")
    keyboard.add(button_menu, button_enter)

    return keyboard


def lesson_list_admin(lessons, grup_num):
    keyboard = InlineKeyboardMarkup(row_width=1)
    for lesson, group in zip(lessons, grup_num):
        button = InlineKeyboardButton(f"{lesson.name}\n{group.base}", callback_data=f"admin/{lesson.Id}")
        keyboard.add(button)
        
    return keyboard


def lesson_info_admin(lesson_id):
    keyboard = InlineKeyboardMarkup(row_width=2)
    begin = InlineKeyboardButton("Провести занятие", callback_data=f"begin/{lesson_id}")
    keyboard.add(button_menu, begin)

    return keyboard

