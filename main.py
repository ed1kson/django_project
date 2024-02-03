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
    ).save()

def get_teacher_by_name(name):
    return Teacher.objects.get(name = name)

def get_student_by_name(name, surname):
    return Student.objects.get(name, surname)

def add_subject(name, teacher_name):
    if not Subject.objects.get(name = name):
        Subject(
            name = name,
            teacher = get_teacher_by_name(teacher_name)
        ).save()

def get_students_in_class(class_name):
    return Student.objects.filter(student_class = get_class_by_name(class_name)).all()

def add_teacher(name, surname, subjects:list|tuple):
    teacher = Teacher(
        name = name,
        surname = surname,
        schedule = WeeklySchedule(
            monday = DailySchedule().save(),
            tuesday = DailySchedule().save(),
            wednesday = DailySchedule().save(),
            thursday = DailySchedule().save(),
            friday = DailySchedule().save() 
        ).save()
    )

    teacher.save()

    for subject_name in subjects:
        Subject.create(name = subject_name, teacher = teacher)
    
def get_subject_by_name(name):
    if Subject.objects.get(name = name):
        return Subject.objects.get(name = name)
    else:
        answer = input('Subjects with such a name does not exist yet. Do you want to add a new one? the current subject will be replaced with a free lesson(yes/no):')
        if answer == 'yes':
            teacher = input('enter the teacher name')
            add_subject(name, teacher)
        else:
            return Subject.objects.get(name = 'no lesson')

def find_teacher_by_subject(subject_name):
    return Teacher.objects.get(id = get_subject_by_name(subject_name).id)

def get_teachers_info():
    return Teacher.objects.all()

def get_subjects_of_teacher(teachers_id):
    return Subject.objects.filter(teacher = teachers_id).all()

def get_class_by_name(class_name):
    return Class.objects.get(name = class_name)

def get_classes_info():
    return Class.objects.all()

def get_classes_plan(class_name):
    classs = get_class_by_name(class_name)
    return WeeklySchedule.objects.get(related_class = classs.id)

def get_teachers_plan(subject_name):
    teacher = Teacher.objects.get(id = get_subject_by_name(subject_name).teacher)
    return teacher

def get_class_by_student(name, surname):
    student = Student.objects.get(name = name, surname = surname)
    return Class.objects.filter(id = student.student_class)

def see_teachers_info():
    table = Table()

    columns = ["№", 'name', 'surname']
    for column in columns:
        table.add_column(column)

    teachers = Teacher.objects.all()

    for teacher in teachers:
        row = []
        for i in teacher:
            row.append(i)
        table.add_row(row)
    
    Console().print(table)

def classes_info():
    table = Table()

    columns = ["№", 'name', 'students']
    for column in columns:
        table.add_column(column)

    classes = Class.objects.all()

    for num, item in enumerate(classes, 1):
        
        row = [num, item.name, len(item.students)]

        table.add_row(row)
    
    Console().print(table)

def add_lesson_to_plan(class_name, day, lesson_number, subject):
    classes_plan = get_classes_plan(class_name)
    teachers_plan = get_teachers_plan(subject)

    if day == 'monday':
        day = classes_plan.monday
    elif day == 'tuesday':
        day = classes_plan.tuesday
    elif day == 'wednesday':
        day = classes_plan.wednesday
    elif day == 'thirsday':
        day = classes_plan.thursday
    elif day == 'friday':
        day = classes_plan.friday

    subject = get_subject_by_name(subject)

    if lesson_number == 1:
        day.first_lesson = subject
    elif lesson_number == 2:
        day.second_lesson = subject
    elif lesson_number == 3:
        day.third_lesson = subject
    elif lesson_number == 4:
        day.fourth_lesson = subject
    elif lesson_number == 5:
        day.fifth_lesson = subject
    elif lesson_number == 6:
        day.sixth_lesson = subject
    elif lesson_number == 7:
        day.seventh_lesson = subject

def func(day):
    for lesson in day:
        yield lesson

def see_classes_plan(class_name):
    table = Table(title=class_name)
    columns = ['№', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    for column in columns:
        table.add_column(column)


    week = WeeklySchedule.objects.get(relation = get_class_by_name(class_name).id)
    for row_num in range(7):
        row = []
        for day in week:
            for lesson_num, lesson in enumerate(day, 1):
                if lesson_num == row_num:
                    row.append(lesson.name)
        table.add_row(row)

    Console().print(table)

def manage_schedule_of_class():
    print('Schedule of what class do you want to change?')
    classes = [(classs.id, classs.name) for classs in get_classes_info()]

    for item in classes:
        print(f'{item[0]}. {item[1]}')
    class_name = input('(enter name of the class): ')

    plan = get_classes_plan(class_name)
    see_classes_plan(class_name)
    
    day = input('Choose a day:')
    lesson = input('Choose a number:')
    subject = input('What subject?:')

    add_lesson_to_plan(class_name, day, lesson, subject)

def see_teachers_schedule(name, surname):
    teacher = get_teacher_by_name(name, surname)


    table = Table(title=class_name)
    columns = ['№', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']

    for column in columns:
        table.add_column(column)


    week = WeeklySchedule.objects.get(relation = teacher.schedule)
    for row_num in range(7):
        row = []
        for day in week:
            for lesson_num, lesson in enumerate(day, 1):
                if lesson_num == row_num:
                    row.append(lesson.name)
                    break
        table.add_row(row)

    Console().print(table)
    

#------------------------------------------------------------------------------------

run = True
question = '''
Welcome to our school!
Pick one of the following actions
1. Add a student
2. Add a teacher 
3. Manage schedule
4. See info about classes 
5. See info about teachers
4. exit 
'''
person = None

while run:
    print(question)
    answer = int(input('Enter a number:'))
    if answer == 1:
        name = input('enter your name:')
        surname = input('enter your surname:')

        print(get_classes_info())
        class_name= input('what class would you like to be in?:')
        add_student(name, surname, class_name)

    elif answer == 2:
        name = input('enter your name:')
        surname = input('enter your surname:')

        print(get_classes_info())
        subjects = input('What subjects do you teach?:').split(', ')
        add_teacher(name, surname, class_name)
    elif answer == 3:
            manage_schedule_of_class()
    elif answer == 4:
        run = False
    else:
        print('please, enter the number from 1 to 4')

