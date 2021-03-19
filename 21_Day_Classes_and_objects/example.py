class Person():
    def __init__(self, name='Diego', second_name='Fregolente', age=24, country='Brazil', city='São Paulo'):
        self.name = name
        self.second_name = second_name
        self.age = age
        self.country = country
        self.city = city
        self.skills = list()

    def person_info(self):
        return f'{self.name} {self.second_name} is at yours {self.age}\'s He lives in {self.country} and {self.city} '

    def add_skills(self, skill):
        self.skills.append(skill)

# p1 = Person()
# print(p1.person_info())
# p1.add_skills('Python')
# p1.add_skills('Gaming')
# p1.add_skills('Driving')
# p2 = Person('Amanda', 'Onofre', 29, 'Brazil', 'São Paulo')
# print(p2.person_info())
# print(p1.skills)
# print(p2.skills)

# Student

class Student(Person):
    def __init__(self, name, second_name, age, country, city, gender):
        self.gender = gender
        super().__init__(name, second_name, age, country, city)

    def person_info(self):
        gender = 'He' if self.gender == 'male' else 'She'
        return f'{self.name} {self.second_name} is {self.age} years old. {gender} lives in {self.country}, {self.city}'

s1 = Student('Diego', 'Fregolente', 24, 'Brazil', 'São Paulo', 'male')
s1.add_skills('Python')
print(s1.person_info())
print(s1.skills)

