from database import User, Lesson

welcome = "Привет!\nПройди регистрацию"
exist = "Ты уже зарегестрировался"

# registration
what_1name = "Как тебя зовут?(имя)"
what_first_name = "Что? Такое имя бывает? Введи твое имя"

what_0name = "Какая фамилия?"
what_last_name = "Что? Такая фамилия бывает? Введи твою фамилию..."

what_group = "Из какой ты группы?\n(полный формат без буквы, пример:4145-020303)"
wrong_group = "Группа введена некорректно, пример: 4145-020303"

nice_recistration = "Регистрация прошла успешно"


wrong_admin = "Самозванец!!!"
#lesson
def lessonInfo(lesson:Lesson):
    text = f"{lesson.name}\n"
    return text

def lessonInfoAdmin(lesson:Lesson, num_record):
    text = f"{lesson.name}\nЗаписалось человек: {num_record}"


list_lessons = "Список доступных экзаменов для сдачи"
into_lesson = "Успешно, как наберется группа я сообщу тебе!"


#notification 
def userNotification(user:User, lesson:Lesson):
    return f"""Привет, {user.first_name}!\n
Ты хотел попробовать сдать пробный экзамен: {lesson.name}.\n
Собралась группа, ждем тебя:\n
Адрес: {lesson.adress}\n
Время: {lesson.date}"""

def adminNotification(lesson:Lesson):
    return f"Хей, группа собралась на экзамен {lesson.name}"



