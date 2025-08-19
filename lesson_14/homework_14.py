class Student:
    def __init__(self, name, surname, age, average_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score


    def update_average_score(self, new_score):
        self.average_score = new_score
        print(f"Average score of student {self.name} {self.surname} was changed to {self.average_score}")

    # мне подсказали, что сделать вывод информации отдельным методом будет лучше
    def display_info(self):
        print(f"Name: {self.name} {self.surname}")
        print(f"Age: {self.age}")
        print(f"Average score: {self.average_score}")



student1 = Student("John", "Doe", 20, 4.5)

print("Student's info:")

student1.display_info()
print("-"*80)

student1.update_average_score(4.8)
print()
print("-"*80)

print("Changed student's info:")
student1.display_info()