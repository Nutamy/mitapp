import csv
import users

class School:
    def __init__(self, name=None, address=None, phone=None, email=None, num_stud=None, num_teachers=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.num_stud = num_stud
        self.num_teachers = num_teachers
        self.list_of_teachers = []
        self.list_of_students = []

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
        self.list_of_students.append(users.Student(name=name, surname=surname, age=age, gender=gender, nationality=nationality, school=school, subject=subject))

    def add_teacher(self, name, surname, age, gender, nationality, school, subject):
        self.num_teachers += 1
        self.list_of_teachers.append(users.Teacher(name=name, surname=surname, age=age, gender=gender, nationality=nationality, school=school, subject=subject))

    def get_info(self):
        info = {'School':self.name, 'Address':self.address, 'Phone':self.phone, 'Email':self.email, 'Number of students':self.num_stud, 'Number of teachers':self.num_teachers}
        return info

    def get_report(self):
        with open(f'{self.name}.csv', 'w') as f:
            writer = csv.writer(f)
            info = self.get_info()
            for key, value in info.items():
                writer.writerow([f"{key} : {value}"])