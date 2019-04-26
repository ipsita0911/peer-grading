from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from .models import *

def getChecker(n, i, m, nq, qno):
    a = []
    for j in range (0,m):
        a.append(((i+j)%n)*nq + qno)
    return a

def index(request):
    message = "The Code Runs!"
    return render(request, 'index.html', {"message":message})

def student_home(request, rollNumber):
    student = Student.objects.get(rollNumber = rollNumber)
    questions = Question.objects.all()
    total_questions = Question.objects.count()
    name = student.name
    programme = student.programme
    department = student.department
    for i in questions:
        print(i.questionID)

    return render(request, 'home.html', {"name":name, "programme":programme, "rollNumber":rollNumber, "department":department, "questions":questions})

def submit_program(request, question_number, rollNumber):
    question = Question.objects.get(questionID=question_number)
    submission = Submission.objects.filter(questionNo=question, rollNumber=rollNumber)
    answer = request.POST[question_number+'answer']
    if not submission:
        new_submission = Submission(questionNo=question, rollNumber=rollNumber, submission=answer)
        new_submission.save()
    else:
        submission.update(submission=answer)
        
    return redirect('/peer/'+rollNumber+'/task_student/')

def to_grade(request, question_number, rollNumber):
    no_of_task = 4
    total_students = Student.objects.count()
    question = Question.objects.get(questionID = question_number)
    total_questions = Question.objects.count()
    submissions = Submission.objects.filter(questionNo = question)
    qid = Submission.objects.filter(rollNumber = rollNumber, questionNo = question_number)
    i = qid[0].uniqueID
    print (i)
    uniqueID = int((i-1)/total_questions) + 1
    print (uniqueID)
    to_check = getChecker(total_students, uniqueID, no_of_task, total_questions, int(question_number))
    print (to_check)
    a = []
    for e in to_check:
        print (e)
        data_dict = {}
        sub = Submission.objects.get(uniqueID = e)
        to_checkStudent = Student.objects.filter(rollNumber = rollNumber).update(submission = sub)
        data_dict["uid"] = e
        data_dict["text"] = sub.submission
        a.append(data_dict)
        data_dict = {}
    print (a)

    return render(request, 'grading.html', {"codes":a, "rollNumber":rollNumber, "question_number":question_number})

def task(request, rollNumber):
    student = Student.objects.get(rollNumber = rollNumber)
    questions = Question.objects.filter()
    submissions = Submission.objects.filter(rollNumber = rollNumber)
    for submission in submissions:
        print (submission.questionNo)
    return render(request, 'task.html', {"questions":questions, "rollNumber":rollNumber})

def grade(request, question_number, uniqueID, rollNumber):
    submission = Submission.objects.get(uniqueID = uniqueID)
    marks = request.POST[uniqueID + 'grade']
    student = Student.objects.get(rollNumber = rollNumber)
    new_marks = Marks(checked_by = student, submission_id=submission, marks = int(marks))
    new_marks.save()
    return redirect('/peer/'+question_number+"/"+rollNumber+'/student/')

    
