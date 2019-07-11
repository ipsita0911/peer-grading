from mongoengine import ReferenceField

class Question(Document):
    questionID = IntField()
    questionText = StringField()

class Student(Document):
    rollNo = IntField()
    programme = StringField()
    department = StringField()
    questions = ListField (ReferenceField(Question))
    marks = ListField (IntField)

class Submission(Document):
    question = RefernceField(Question)
    student = ReferenceField(Student)
    submission = StringField()
    checkedBy = ListField(ReferenceField(Student))