class Student:

    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def stud_info(self):
        return 'name: ',self.name,', age: ',str(self.age),', major: ',self.major

Steve = ''.join(Student('Steven Schultz', 23, 'English').stud_info())
Johnny = ''.join(Student('Jonathan Rosenberg', 24, 'Biology').stud_info())
Penny = ''.join(Student('Penelope Meramveliotakis', 21, 'Physics').stud_info())

print(Steve)
print(Johnny)
print(Penny)
