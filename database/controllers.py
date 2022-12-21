from .dataBase import data_base
from .models import (User, Lesson, Admins, Recording, Group)
from peewee import DoesNotExist


class UserControll:
    def __init__(self):
        pass

    def add(self, user:User):
        user.save()


    def delete(self, user:User):
        user.delete_instance()
        user.save()

    
    def findById(self, Id=None, telegram_id=None):
        if(Id is not None):
            return (User.select().where(User.Id == Id))
        if(telegram_id is not None):
            return (User.select().where(User.telegram_id==telegram_id))
        return None


    def exist(self, Id=None, telegram_id=None):
        return bool(self.findById(Id, telegram_id))


class LessonControll:
    def add(self, lesson:Lesson):
        lesson.save()

 
    def delete(self, lesson:Lesson):
        lesson.delete_instance()
        lesson.save()


    def findById(self, lesson_id):
        return (Lesson.select().where(Lesson.Id == lesson_id))


    def findByGroupId(self, group_id:int):
        return (Lesson.select().where(Lesson.group_id == group_id))


    def exist(self, lesson_id:int):
        return bool(self.findById(lesson_id))



class RecordingControll:
    def add(self, rec:Recording):
        if(not self.exist(rec.user_id, rec.lesson_id)):
            rec.save()


    def delete(self, rec:Recording):
        rec.delete_instance()
        rec.save()


    def find(self, user_id, lesson_id):
        return (Recording.select().where(Recording.lesson_id == lesson_id and Recording.user_id == user_id))


    def exist(self, user_id, lesson_id):
        return bool(self.find(user_id, lesson_id))



class AdminControll:
    pass

def create_tables():
    with data_base:
        data_base.create_tables([User, Lesson, Group, Recording, Admins])


def groupFindId(group):
    try:
        return (Group.get(Group.group_base == group))
    except(DoesNotExist):
        return -1

def isAdmin(telegram_id):
    return bool(Admins.select().join(User, on=User.Id==Admins.user_id ).where(User.telegram_id == telegram_id))
