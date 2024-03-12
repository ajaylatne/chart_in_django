from django.db import models


class Student(models.Model):
    student_name = models.CharField(max_length=20)


class Language(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='lang')
    python = models.PositiveIntegerField()
    java = models.PositiveIntegerField()
    js = models.PositiveIntegerField()
    c = models.PositiveIntegerField()
    sql = models.PositiveIntegerField()
