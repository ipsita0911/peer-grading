from nosql_models.models import *
from mongoengine import connect

connect('testing_puppy')

def checkedBy( tobeChecked, totalStudents, totalCheckers):
    checkers = []
    for checker in range (0,totalCheckers):
        checkers.append( (tobeChecked + checker) % totalStudents )
    return checkers

def homepage(request, rollNumber):
    student = Student.objects.get(rollNo = rollNo)
    questions = student.questions.all()
    total_questions = questions.count
    name = student.name
    programme = student.programme
    department = student.department
    for question in questions:
        print(question.questionID)

    return render(request, 'home.html', {"name":name, "programme":programme, "rollNumber":rollNumber, "department":department, "questions":questions})

def gradedBy (request, questionID):
    submissions = []
    question = Question.objects.get(questionID = questionID)
    for submission in Submission.objects.get(question = question):
        submissions.append(submission)

    totalSubmissions = submissions.count

    random.shuffle(submissions)

    for submission in range (0,totalSubmissions):
        checkers = []
        for checker in checkedBy(submission, totalSubmissions, totalCheckers):
            checkers.append(checker)
        for checker in checkers:
            submissions[submission].checkedBy.append(submissions[checker])

        



    