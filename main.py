import django_setup
from myapp.models import Teacher, Subject, Student, Class, WeeklySchedule, DailySchedule, Note
from rich.console import Console
from rich.table import Table

def add_class(name):
    days = []

    for i in range(5):
        days.append(DailySchedule())
    
    week = WeeklySchedule(
        monday = days[0],
        tuesday = days[1],
        wednesday = days[2],
        thursday = days[3],
        friday = days[4]
    )

    the_class = Class(name = name, schedule = week)
    for day in days:
        day.save()

    week.save()
    the_class.save()

def get_class_by_name(name):
    return Class.objects.get(name = name)

def add_student(name, surname, the_class):
    Student(
        name = name,
        surname = surname, 
        student_class = get_class_by_name(the_class)
    ).save()

def get_teacher_by_name(name, surname):
    return Teacher.objects.get(name = name, surname = surname)

def get_student_by_name(name, surname):
    return Student.objects.get(name = name, surname = surname)

def add_subject(name):
    if not Subject.objects.get(name = name):
        subject = Subject(
            name = name,
        )
        subject.save()
        print(get_teachers_info())
        name, surname = (input("teacher?(leave it empty if no):")).split()
        if answer != '':
            teacher = get_teacher_by_name(name, surname)
            subject.teacher.add(teacher)
    else:
        print('already exists')

def get_students_in_class(class_name):
    return Student.objects.filter(student_class = get_class_by_name(class_name)).all()

def add_teacher(name, surname, subject_names:list|tuple):
    days = []
    
    for i in range(5):
        days.append(DailySchedule())

    schedule = WeeklySchedule(
            monday = days[0],
            tuesday = days[1],
            wednesday = days[2],
            thursday = days[3],
            friday = days[4] 
        )
    
    teacher = Teacher(
        name = name,
        surname = surname,
        schedule = schedule
    )
    for i in days:
        i.save()
    schedule.save()
    teacher.save()
    subjects = [item.name for item in Subject.objects.all()]
    for item in subject_names:
        if item not in subjects:
            subject = Subject.objects.create(name = item)
            subject.teacher.add(teacher)
        else:
            subject = get_subject_by_name(name = item)
            subject.teacher.add(teacher)
    
def get_subject_by_name(name):
    if Subject.objects.get(name = name):
        return Subject.objects.get(name = name)
    else:
        answer = input('Subjects with such a name does not exist yet. Do you want to add a new one? the current subject will be replaced with a free lesson(yes/no):')
        if answer == 'yes':
            add_subject()
        else:
            return Subject.objects.get(name = 'no lesson')

def find_teacher_by_subject(subject_name):
    return Teacher.objects.get(id = get_subject_by_name(subject_name).id)

def get_teachers_info():
    teachers = Teacher.objects.all()
    for i in teachers:
        sbs = ', '.join([subject.name for subject in i.subjects.all()])
        print(f'1. {i.name} {i.surname}, teaches: {sbs}')

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
    teachers = Subject.objects.get(name = subject_name).teacher.all()
    if len(teachers) == 0:
        print(f'there is no subject named {subject_name} or no one wants to deal with it')
    elif len(teachers) > 1:
        print('there are multiple teachers teaching this lesson. Which one do you want to get busy?')
        for teacher in teachers:
            print(f'1. {teacher.name, teacher.surname}')
        name, surname = input('enter name and surname (name surname)').split()
        return get_teacher_by_name(name, surname)
    elif len(teachers) == 1:
        name, surname = teacher[0].name, teacher[1].surname
        return get_teacher_by_name(name, surname)

def get_class_by_student(name, surname):
    student = Student.objects.get(name = name, surname = surname)
    return Class.objects.filter(id = student.student_class)

def see_teachers_info():
    table = Table()

    columns = ["№", 'name', 'surname', 'subjects']
    for column in columns:
        table.add_column(column)

    teachers = Teacher.objects.all()

    for num, teacher in enumerate(teachers, 2):
        subjects = ', '.join([subject.name for subject in teacher.subjects.all()])
        table.add_row(str(num), teacher.name, teacher.surname, subjects)
    
    Console().print(table)

def classes_info():
    table = Table()

    columns = ["№", 'name', 'students']
    for column in columns:
        table.add_column(column)

    classes = Class.objects.all()

    for num, item in enumerate(classes, 1):
        table.add_row(str(num), item.name, str(len(item.students.all())))
    
    Console().print(table)

def add_lesson_to_plan(class_name, day, lesson_number, subject):
    classes_plan = get_classes_plan(class_name)
    teachers_plan = get_teachers_plan(subject)
    if day == 'monday':
        day = classes_plan.monday
        day2 = teachers_plan.monday
    elif day == 'tuesday':
        day = classes_plan.tuesday
        day2 = teachers_plan.tuesday
    elif day == 'wednesday':
        day = classes_plan.wednesday
        day2 = teachers_plan.wednesday
    elif day == 'thirsday':
        day = classes_plan.thursday
        day2 = teachers_plan.tuesday
    elif day == 'friday':
        day = classes_plan.friday
        day2 = teachers_plan.tuesday

    subject = get_subject_by_name(subject)
    lesson_number = int(lesson_number)

    if lesson_number == 1:
        day.first_lesson = subject
        day2.first_lesson = subject
    elif lesson_number == 2:
        day.second_lesson = subject
        day2.second_lesson = subject
    elif lesson_number == 3:
        day.third_lesson = subject
        day2.third_lesson = subject
    elif lesson_number == 4:
        day.fourth_lesson = subject
        day2.fourth_lesson = subject
    elif lesson_number == 5:
        day.fifth_lesson = subject
        day2.fifth_lesson = subject
    elif lesson_number == 6:
        day.sixth_lesson = subject
        day2.sixth_lesson = subject
    elif lesson_number == 7:
        day.seventh_lesson = subject
        day2.seventh_lesson = subject
    day.save()
    day2.save()


def see_classes_plan(class_name):
    table = Table(title=class_name)
    columns = ['№', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    for column in columns:
        table.add_column(column)


    week = WeeklySchedule.objects.get(related_class = get_class_by_name(class_name).id).as_list()
    for row_num in range(1, 8):
        row = [str(row_num)]
        for day in week:
            for lesson_num, lesson in enumerate(day.as_list(), 1):
                if lesson_num == row_num:
                    row.append(lesson.name)
        table.add_row(*row)

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

def see_teachers_plan(name, surname):
    teacher = get_teacher_by_name(name, surname)


    table = Table(title=name+' '+surname)
    columns = ['№', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']

    for column in columns:
        table.add_column(column)


    week = WeeklySchedule.objects.get(related_teacher = teacher.schedule).as_list()
    for row_num in range(1, 8):
        row = [str(row_num)]
        for day in week:
            for lesson_num, lesson in enumerate(day.as_list(), 1):
                if lesson_num == row_num:
                    row.append(lesson.name)
                    break
        table.add_row(*row)

    Console().print(table)

def give_note(student_name, student_surname, subject_name, note):
    student = get_student_by_name(student_name, student_surname)
    subject = get_subject_by_name(subject_name)

    Note.objects.create(note = note, student = student, subject = subject)

def get_notes_of_student(name, surname):
    table = Table(title=' '.join([name, surname]))

    table.add_column('subject')
    table.add_column('note')
    
    student = get_student_by_name(name, surname)
    for note in student.notes.all():
        subject = str(note.subject)
        note = str(note.note)
        table.add_row(subject, note)
    
    Console().print(table)


#------------------------------------------------------------------------------------

run = True
question = '''
Pick one of the following actions
1. Add a student
2. Add a teacher 
3. Manage schedule
4. See info about classes 
5. See info about teachers
6. Give a note to a student 
7. See students notes
8. create a class
9. add a subject
10. see classes plan
0. exit 
'''

person = None

while run:
    print(question)
    answer = int(input('Enter a number:'))
    if answer == 1:
        name = input('enter students name:')
        surname = input('enter students surname:')

        print(get_classes_info())
        class_name= input('what class would you like to be in?:')
        add_student(name, surname, class_name)

    elif answer == 2:
        name = input('enter teachers name:')
        surname = input('enter teachers surname:')

        print(get_classes_info())
        subjects = input('What subjects do you teach?(subject1, subject2, subject3):').split(', ')
        add_teacher(name, surname, subjects)
    elif answer == 3:
            manage_schedule_of_class()
    elif answer == 4:
        classes_info()
    elif answer == 5:
        get_teachers_info()
    elif answer == 6:
        students_name = input('enter the students name:')
        students_surname = input('enter the students surname:')
        subject_name = input('enter the subjects name:')
        note = int(input('enter the note:'))
        give_note(students_name, students_surname, subject_name, note)
    elif answer == 7:
        name = input('input students name:')
        surname = input('input students surname:')
        get_notes_of_student(name, surname)
    elif answer == 8:
        grade = input('Enter classes grade:')
        letter = input('Enter classes identifier(A-Z):')
        add_class(grade+letter)
    elif answer == 9:
        surname
        add_subject()
    elif answer == 10:
        classes_info()
        class_name = input('enter classes name')
        see_classes_plan(class_name)
    elif answer == 11:
        see_teachers_info()
        name = input('enter name:')
        surname = input('enter surname:')
        see_teachers_plan(name, surname)
    elif answer == 0:
        run = False
    else:
        print('please, enter the number from 1 to 4')
