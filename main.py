import django_setup
from myapp.models import Teacher, Subject, Student, Class, WeeklySchedule, DailySchedule
from rich.console import Console
from rich.table import Table

def add_class(name):
    default = get_subject_by_name("no lesson")
    plan = WeeklySchedule(
        monday = DailySchedule(default).save(),
        tuesday = DailySchedule(default).save(),
        wednesday = DailySchedule(default).save(),
        thursday = DailySchedule(default).save(),
        friday = DailySchedule(default).save()
    )
    the_class = Class(name = name, schedule = plan)

    plan.save()
    the_class.save()

def get_class_by_name(name):
    return Class.objects.get(name = name)

def add_student(name, surname, the_class):
    Student(
        name = name,
        surname = surname, 
        student_class = get_class_by_name(the_class)
    )

def get_teacher_by_name(name):
    return Teacher.objects.get(name = name)

def get_student_by_id(id):
    return Student.objects.get(id = id)

def add_subject(name, teacher_name):
    Subject(
        name = name,
        teacher = get_teacher_by_name(teacher_name)
    )

def get_students_in_class(class_name):
    return Student.objects.filter(student_class = get_class_by_name(class_name)).all()

def add_teacher(name, surname, subjects:list|tuple):
    teacher = Teacher(name = name, surname = surname)
    teacher.save()

    for subject_name in subjects:
        Subject.create(name = subject_name, teacher = teacher)
    
def get_subject_by_name(name):
    return Subject.objects.get(name = name)

def find_teacher_by_subject(subject_name):
    return Teacher.objects.get(id = get_subject_by_name(subject_name).id)

def get_teachers_info():
    return Teacher.objects.all()

def get_subjects_of_teacher(teachers_id):
    return Subject.objects.filter(teacher = teachers_id)

def get_class_by_name(class_name):
    return Class.objects.get(name = class_name)

def get_classes_plan(class_name):
    classs = get_class_by_name(class_name)
    return WeeklySchedule.objects.get(related_class = classs.id)

def add_lesson_to_plan(class_name, day, lesson_number, subject):
    plan = get_classes_plan(class_name)

    if day == 'monday':
        day = plan.monday
    elif day == 'tuesday':
        day = plan.tuesday
    elif day == 'wednesday':
        day = plan.wednesday
    elif day == 'thirsday':
        day = plan.thursday
    elif day == 'friday':
        day = plan.friday

    if lesson_number == 1:
        day.first_lesson = get_subject_by_name(subject)
    elif lesson_number == 2:
        day.second_lesson = get_subject_by_name(subject)
    elif lesson_number == 3:
        day.third_lesson = get_subject_by_name(subject)
    elif lesson_number == 4:
        day.fourth_lesson = get_subject_by_name(subject)
    elif lesson_number == 5:
        day.fifth_lesson = get_subject_by_name(subject)
    elif lesson_number == 6:
        day.sixth_lesson = get_subject_by_name(subject)
    elif lesson_number == 7:
        day.seventh_lesson = get_subject_by_name(subject)

def see_classes_plan(class_name):
    table = Table(title=class_name)
    columns = ['№', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    for column in columns:
        table.add_column(column)

    week = WeeklySchedule.objects.get(related_class = get_class_by_name(class_name).id)
    for number, day in enumerate(week, 1):
        row = [number]

        for subject in day:
            row.append(subject.name)
        
        table.add_row(row)

    Console().print(table)

#------------------------------------------------------------------------------------

run = True
question = '''
Welcome to our school!
Pick one of the following actions
1. Log in
2. Add a student
3. Add a teacher 
4. Manage schedule
5. 
6.
7.
8.
'''
while run:
    print(question)
