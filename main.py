import django_setup
from myapp.models import Teacher, Subject, Student, Class

def add_class(name):
    Class.objects.create(name = name)

def get_class_by_name(name):
    return Class.objects.get(name = name)

def add_student(name, surname, the_class):
    Student(
        name = name,
        surname = surname, 
        student_class = get_class_by_name(the_class)
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

#------------------------------------------------------------------------------------
run = True
while run:
    pass