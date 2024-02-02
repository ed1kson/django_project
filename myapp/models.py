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
    schedule = models.OneToOneField('WeeklySchedule', on_delete = models.DO_NOTHING, related_name = 'related_class')

    def __str__(self):
        return self.name

class WeeklySchedule(models.Model):
    monday = models.OneToOneField('DailySchedule', on_delete = models.DO_NOTHING, related_name = 'related_schedule')
    tuesday = models.OneToOneField('DailySchedule', on_delete = models.DO_NOTHING, related_name = 'related_schedule')
    wednesday = models.OneToOneField('DailySchedule', on_delete = models.DO_NOTHING, related_name = 'related_schedule')
    thursday= models.OneToOneField('DailySchedule', on_delete = models.DO_NOTHING, related_name = 'related_schedule')
    friday = models.OneToOneField('DailySchedule', on_delete = models.DO_NOTHING, related_name = 'related_schedule')

class DailySchedule(models.Model):
    first_lesson = models.ForeignKey(Subject, related_name = "lessons", on_delete = models.DO_NOTHING)
    second_lesson = models.ForeignKey(Subject, related_name = "lessons", on_delete = models.DO_NOTHING)
    third_lesson = models.ForeignKey(Subject, related_name = "lessons", on_delete = models.DO_NOTHING)
    fourth_lesson = models.ForeignKey(Subject, related_name = "lessons", on_delete = models.DO_NOTHING)
    fifth_lesson = models.ForeignKey(Subject, related_name = "lessons", on_delete = models.DO_NOTHING)
    sixth_lesson = models.ForeignKey(Subject, related_name = "lessons", on_delete = models.DO_NOTHING)
    seventh_lesson = models.ForeignKey(Subject, related_name = "lessons", on_delete = models.DO_NOTHING)