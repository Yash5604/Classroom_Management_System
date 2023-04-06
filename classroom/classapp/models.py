from django.db import models
from django.conf import settings

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    p_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = 'classapp_user'

class Classroom(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=50, null=True)
    room = models.CharField(max_length=20)
    subject_name = models.TextField()
    join_code = models.CharField(max_length=7)

    class Meta:
        db_table = 'classapp_classroom'

class Teacher(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

class Student(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)