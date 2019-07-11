from mongoengine import *

class Question (Document):
    questionID = IntField()
    questionText = StringField()

class Student (Document):
    rollNo = IntField()
    programme = StringField()
    department = StringField()
    questions = ListField (ReferenceField (Question) )

class Submission (Document):
    question = ReferenceField(Question)
    student = ReferenceField (Student)
    submission = StringField()
    checkedBy = ListField (ReferenceField (Student))