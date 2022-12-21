import periphery as pr
import database as db

def start(teleg_id):
    user = db.UserControll().exist(telegram_id=teleg_id)
    if(user):
        return pr.exist

    return pr.welcome


def menu_list(teleg_id:int):
    user = db.UserControll().findById(telegram_id=teleg_id)[0]
    lessons = db.LessonControll().findByGroupId (user.group_id)

    keyboard = pr.lessons_list(lessons)
    return (pr.list_lessons, keyboard)


def look_lesson(lesson_id:str):
    lesson_id = int(lesson_id.split("/")[1])
    lesson = db.LessonControll().findById(lesson_id)[0]

    keyboard = pr.lesson_enter(lesson_id)
    message = pr.lessonInfo(lesson)
    
    return (message, keyboard)


def enter_lesson(teleg_id, lesson_id:str):
    lesson_id = int(lesson_id.split("/")[1])

    record = db.Recording()
    record.user_id = db.UserControll().findById(telegram_id=teleg_id)[0].Id
    record.lesson_id = db.LessonControll().findById(lesson_id)[0].Id
    db.RecordingControll().add(record)

    return pr.into_lesson

