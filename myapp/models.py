from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length = 30)
    surname = models.CharField(max_length = 40)
    schedule = models.OneToOneField('WeeklySchedule', on_delete = models.DO_NOTHING, related_name = 'related_teacher')

    def __str__(self): 
        return self.name+' '+self.surname
    

class Subject(models.Model):
    name = models.CharField(max_length = 30, unique = True)
    teacher = models.ManyToManyField(Teacher, related_name='subjects')

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
    schedule = models.OneToOneField('WeeklySchedule', on_delete = models.DO_NOTHING, related_name = 'related_class')

    def __str__(self):
        return self.name
    
    def as_list(self):
        return [self.name, self.schedule]

class WeeklySchedule(models.Model):
    monday = models.OneToOneField('DailySchedule', on_delete = models.DO_NOTHING, related_name = 'mondays')
    tuesday = models.OneToOneField('DailySchedule', on_delete = models.DO_NOTHING, related_name = 'tuesdays')
    wednesday = models.OneToOneField('DailySchedule', on_delete = models.DO_NOTHING, related_name = 'wednesdays')
    thursday= models.OneToOneField('DailySchedule', on_delete = models.DO_NOTHING, related_name = 'thursdays')
    friday = models.OneToOneField('DailySchedule', on_delete = models.DO_NOTHING, related_name = 'fridays')

    def as_list(self):
        return [self.monday, self.tuesday, self.wednesday, self.thursday, self.friday]

class DailySchedule(models.Model):
    first_lesson = models.ForeignKey(Subject, related_name = "firsts", on_delete = models.DO_NOTHING, default = 0)
    second_lesson = models.ForeignKey(Subject, related_name = "seconds", on_delete = models.DO_NOTHING, default = 0)
    third_lesson = models.ForeignKey(Subject, related_name = "thirds", on_delete = models.DO_NOTHING, default = 0)
    fourth_lesson = models.ForeignKey(Subject, related_name = "fourths", on_delete = models.DO_NOTHING, default = 0)
    fifth_lesson = models.ForeignKey(Subject, related_name = "fifths", on_delete = models.DO_NOTHING, default = 0)
    sixth_lesson = models.ForeignKey(Subject, related_name = "sixths", on_delete = models.DO_NOTHING, default = 0)
    seventh_lesson = models.ForeignKey(Subject, related_name = "sevenths", on_delete = models.DO_NOTHING, default = 0)

    def as_list(self):
        return [self.first_lesson, self.second_lesson, self.third_lesson, self.fourth_lesson, self.fifth_lesson, self.sixth_lesson, self.seventh_lesson]

class Note(models.Model):
    student = models.ForeignKey(Student, related_name = 'notes', on_delete = models.DO_NOTHING)
    subject = models.ForeignKey(Subject, related_name = 'notes', on_delete = models.DO_NOTHING)
    note = models.IntegerField(validators = [MaxValueValidator(12), MinValueValidator(1)])
