from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length = 30)
    surname = models.CharField(max_length = 40)
    

    def __str__(self):
        return self.surname
    
class Subject(models.Model):
    name = models.CharField(max_length = 30, unique = True)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, related_name='subjects')
    
    def __str__(self):
        return self.name

#-----------------------------------------------------------------------------------------------

class Student(models.Model):
    name = models.CharField(max_length = 30)
    surname = models.CharField(max_length = 40)
    student_class = models.ForeignKey('Class', on_delete=models.DO_NOTHING, related_name='students')

    def __str__(self):
        return self.surname


class Class(models.Model):
    name = models.CharField(max_length = 30, unique = True)


