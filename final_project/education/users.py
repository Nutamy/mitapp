import csv

class Human:

    def __init__(self, name = None, surname = None, age = None, gender = None, nationality = None):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.nationality = nationality
    
    def set_name(self, name):
        self.name = name

    def set_family(self, surname):
        self.surname = surname

    def set_age(self, age):
        self.age = age

    def set_gender(self, gender):
        self.gender = gender

    def set_nationality(self, nationality):
        self. nationality = nationality

    def get_info(self):
        info = {"Name":self.name, "Surname":self.surname, "Age":self.age, "Gender":self.gender, "Nationality":self.nationality}
        return info

class Teacher(Human):

    list_of_teachers = []

    def __init__(self, name, surname, age, gender, nationality, school = None, subject = None):
        self.school = school
        self.subject = list(subject)
        super().__init__(name, surname, age, gender, nationality)
        Teacher.list_of_teachers.append(self)

    def set_school(self, school):
        self.school = school

    def add_subject(self, *subject):
        for i in range(len(subject)):
            self.subject.append(subject[i])
    
    def get_info(self):
        teacher_info = super().get_info()
        teacher_info['School'] = self.school
        teacher_info['Subjects'] = self.subject
        return teacher_info

    @staticmethod
    def get_info_teachers():
        with open('reports/Teachers.csv', 'w') as f:
            writer = csv.writer(f)
            info = Teacher.list_of_teachers
            for v in info:
                writer.writerow([v.get_info()["Name"], v.get_info()["Surname"], v.get_info()["Age"], v.get_info()["Gender"], v.get_info()["Nationality"], v.get_info()["School"], ''.join(v.get_info()["Subjects"])])

class Student(Teacher):

    list_of_students = []

    def __init__(self, name, surname, age, gender, nationality, school, subject):
        super().__init__(name, surname, age, gender, nationality, school, subject)
        Student.list_of_students.append(self)
        super().list_of_teachers.pop()

    @staticmethod
    def get_info_students():
        with open('reports/Students.csv', 'w') as f:
            writer = csv.writer(f)
            info = Student.list_of_students
            for v in info:
                writer.writerow([v.get_info()["Name"], v.get_info()["Surname"], v.get_info()["Age"], v.get_info()["Gender"], v.get_info()["Nationality"], v.get_info()["School"],  ''.join(v.get_info()["Subjects"])])
    
    



