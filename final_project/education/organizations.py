import csv
from .users import *

class School:
    list_of_schools = []

    def __init__(self, name=None, address=None, phone=None, email=None, num_stud=None, num_teachers=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.num_stud = num_stud
        self.num_teachers = num_teachers
        self.list_of_teachers = []
        self.list_of_students = []
        School.list_of_schools.append(self)

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_phone(self, phone):
        self.phone = phone

    def set_email(self, email):
        self.email = email

    def set_num_stud(self, num_stud):
        self.num_stud = num_stud

    def set_num_teachers(self, num_teachers):
        self.num_teachers = num_teachers

    def add_student(self, name, surname, age, gender, nationality, school, subject):
        self.num_stud += 1
        self.list_of_students.append(Student(name=name, surname=surname, age=age, gender=gender, nationality=nationality, school=school, subject=subject))

    def add_teacher(self, name, surname, age, gender, nationality, school, subject):
        self.num_teachers += 1
        self.list_of_teachers.append(Teacher(name=name, surname=surname, age=age, gender=gender, nationality=nationality, school=school, subject=subject))

    def get_info(self):
        info = {'School':self.name, 'Address':self.address, 'Phone':self.phone, 'Email':self.email, 'Number of students':self.num_stud, 'Number of teachers':self.num_teachers}
        return info

    def get_report(self):
        with open(f'reports/{self.name}.csv', 'w') as f:
            writer = csv.writer(f)
            info = self.get_info()
            for key, value in info.items():
                writer.writerow([f"{key} : {value}"])
            writer.writerow(["Name", "Surname", "Age", "Gender", "Nationality", "School", "Subjects"])
            for v in self.list_of_students:
                writer.writerow([v.get_info()["Name"], v.get_info()["Surname"], v.get_info()["Age"], v.get_info()["Gender"], v.get_info()["Nationality"], v.get_info()["School"], ''.join(v.get_info()["Subjects"])])


    def get_list_of_students(self):
        for student in self.list_of_students:
            return student.get_info()

    def get_report_of_students(self):
        with open(f'reports/{self.name}_students.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Surname", "Age", "Gender", "Nationality", "School", "Subjects"])
            for v in self.list_of_students:
                writer.writerow([v.get_info()["Name"], v.get_info()["Surname"], v.get_info()["Age"], v.get_info()["Gender"], v.get_info()["Nationality"], v.get_info()["School"], ''.join(v.get_info()["Subjects"])])

    def get_list_of_teachers(self):
        return self.list_of_teachers

    def get_report_of_teachers(self):
        with open(f'reports/{self.name}_teachers.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Surname", "Age", "Gender", "Nationality", "School", "Subjects"])
            for v in self.list_of_teachers:
                writer.writerow([v.get_info()["Name"], v.get_info()["Surname"], v.get_info()["Age"], v.get_info()["Gender"], v.get_info()["Nationality"], v.get_info()["School"], ''.join(v.get_info()["Subjects"])])

    @staticmethod
    def get_info_schools():
        with open('reports/Schools.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['School', 'Address', 'Phone', 'Email', 'Number of students', 'Number of teachers'])
            for v in School.list_of_schools:
                writer.writerow([v.get_info()["School"], v.get_info()["Address"], v.get_info()["Phone"], v.get_info()["Email"], v.get_info()["Number of students"], v.get_info()["Number of teachers"]])

#name=None, address=None, phone=None, email=None, num_stud=None, num_teachers=None
