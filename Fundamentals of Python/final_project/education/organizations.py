import os
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

        if os.path.exists(f'reports/{self.name}.csv'):
            f = open(f'reports/{self.name}.csv', 'r')
            reader = csv.reader(f)
            for row in reader:
                if row[0] == 'Teacher':
                    self.num_teachers += 1
                    self.list_of_teachers.append(Teacher(name=row[1], surname=row[2], age=row[3], gender=row[4], nationality=row[5], school=row[6], subject=row[7]))
                elif row[0] == 'Student':
                    self.num_stud += 1
                    self.list_of_students.append(Student(name=row[1], surname=row[2], age=row[3], gender=row[4], nationality=row[5], school=row[6], subject=row[7]))

            

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
        if name==None or surname==None or age==None or gender==None or nationality==None or school==None or subject==None:
            print("Fill all the information about the person")
        else:
            student = Student(name=name, surname=surname, age=age, gender=gender, nationality=nationality, school=school, subject=subject)
            if student in self.list_of_students:
                print("This person has already exist in the table.")
            else:
                self.num_stud += 1
                self.list_of_students.append(student)


    def add_teacher(self, name, surname, age, gender, nationality, school, subject):
        if name==None or surname==None or age==None or gender==None or nationality==None or school==None or subject==None:
            print("Fill all the information about the person")
        else:
            teacher = Teacher(name=name, surname=surname, age=age, gender=gender, nationality=nationality, school=school, subject=subject)
            if teacher in self.list_of_teachers:
                print("This person has already exist in the table.")
            else:
                self.num_teachers += 1
                self.list_of_teachers.append(teacher)


    def get_info(self):
        info = {'School':self.name, 'Address':self.address, 'Phone':self.phone, 'Email':self.email, 'Number of students':self.num_stud, 'Number of teachers':self.num_teachers}
        return info

    def get_report(self):
        with open(f'reports/{self.name}.csv', 'w') as f:
            writer = csv.writer(f)
            info = self.get_info()
            #Записываем информацию о школе
            writer.writerow(['School', 'Address', 'Phone', 'Email', 'Number of students', 'Number of teachers'])
            writer.writerow([info['School'], info['Address'], info['Phone'], info['Email'], info['Number of students'], info['Number of teachers']])

            for v in self.list_of_students:
                writer.writerow([v.csv_type, v.get_info()["Name"], v.get_info()["Surname"], v.get_info()["Age"], v.get_info()["Gender"], v.get_info()["Nationality"], v.get_info()["School"], v.get_info()["Subjects"]])

            for v in self.list_of_teachers:
                writer.writerow([v.csv_type, v.get_info()["Name"], v.get_info()["Surname"], v.get_info()["Age"], v.get_info()["Gender"], v.get_info()["Nationality"], v.get_info()["School"], v.get_info()["Subjects"]])

    def get_list_of_teachers(self):
        list_of_teachers = self.list_of_teachers
        for obj in list_of_teachers:
            print(obj.get_info())

    def get_list_of_students(self):
        list_of_students = self.list_of_students
        for obj in list_of_students:
            print(obj.get_info())

    def get_report_my_school(self):
        with open(f'reports/{self.name}_info.csv', 'w') as f:
            writer = csv.writer(f)
            info = self.get_info()
            for key, value in info.items():
                writer.writerow([f"{key} : {value}"])

