from django.shortcuts import render
from .models import Student
from django.shortcuts import render


def index(request):
    students = Student.objects.all()
    student_wise_skill = {}
    for student in students:
        student_wise_skill[student] = student.lang.all()[0]
    out = list(student_wise_skill.items())
    final_list = []
    for stu, lang in out:

        student_lang_prof = [
            {"label": "Python", "y": lang.python},
            {"label": "Java", "y": lang.java},
            {"label": "C", "y": lang.c},
            {"label": "JS", "y": lang.js},
            {"label": "SQL", "y": lang.sql},
        ]
        temp_dict = (stu, student_lang_prof)
        final_list.append(temp_dict)

    return render(request, 'index.html', {"final_list": final_list})
