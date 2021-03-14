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

    def __init__(self, name, surname, age, gender, nationality, school = None, subject = None):
        self.school = school
        self.subject = list(subject)
        super().__init__(name, surname, age, gender, nationality)

    def set_school(self, school):
        self.school = school

    def add_subject(self, *subject):
        for i in range(len(subject)):
            self.subject.append(subject[i])
    
    def get_info(self):
        student_info = super().get_info()
        student_info['School'] = self.school
        student_info['Subjects'] = self.subject
        return student_info

class Student(Teacher):

    def __init__(self, name, surname, age, gender, nationality, school, subject):
        super().__init__(name, surname, age, gender, nationality, school, subject)


    
    



