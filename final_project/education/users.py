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

    



