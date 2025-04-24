class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Yo, I’m {self.name} and I’m {self.age} years old.")
        
    def is_adult(self):
        return self.age >= 18


        
fuad = Person("Fuad", 23)
fuad.greet()  # Output: Yo, I’m Fuad and I’m 23 years old.
if fuad.is_adult():
    print("Fuad is grown.")
    
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def show_id(self):
        print("Student ID:", self.student_id)
sami = Student("Sami", 22, "DIU2025")
sami.greet()
sami.show_id()
