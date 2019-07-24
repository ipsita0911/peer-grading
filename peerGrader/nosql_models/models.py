from mongoengine import *

class Question (Document):
    questionID = IntField()
    questionText = StringField()

class Student (Document):
    rollNo = IntField()
    programme = StringField()
    department = StringField()

class Submission (Document):
    question = ReferenceField(Question)
    student = ReferenceField (Student)
    submission = StringField()
    grading = ListField({"checkedBy" : ReferenceField(Student), "marks" : IntField()})