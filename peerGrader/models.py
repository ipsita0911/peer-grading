from django.db import models

# Create your models here.

class Question(models.Model):

    questionID = models.AutoField(primary_key = True)
    question_text = models.CharField(max_length=10000)

    def __str__(self):
        return str(self.questionID)


class Submission(models.Model):

    questionNo = models.ForeignKey(Question, on_delete = models.CASCADE)
    uniqueID = models.AutoField(primary_key = True)
    rollNumber = models.IntegerField(default=0, blank=True)
    submission = models.CharField(max_length = 50)

    def __str__(self):
        return str(self.uniqueID)

class Student(models.Model):

    name = models.CharField(max_length = 50)
    rollNumber = models.IntegerField(primary_key = True)
    programme = models.CharField(max_length = 50)
    department = models.CharField(max_length = 50)
    submission = models.ForeignKey(Submission, on_delete = models.CASCADE, blank=True, null=True)
    def __str__(self):
        return str(self.rollNumber)

class Marks(models.Model):

    submission_id = models.ForeignKey(Submission, on_delete = models.CASCADE)
    checked_by = models.ForeignKey(Student, on_delete = models.CASCADE)
    marks = models.IntegerField(default = -1, blank = True, null = True)

