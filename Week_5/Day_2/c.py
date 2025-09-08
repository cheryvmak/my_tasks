

# Nigerian School Management System
from abc import ABC, abstractmethod

class SchoolMember(ABC):
    def __ini__(self,  name, id_number):

        self._name = name     # Encapsulation  - protected attribute
        self._id_number = id_number  # Encapsulation - protected attribute

    @abstractmethod
    def daily_activity(self):     # Abstraction - must be implemented
        pass

    def get_info(self):
        return f"Name: {self._name}, ID: {self._id_number}"
    
    # Inheritance - Student inherits from SchoolMember
class Student(SchoolMember):
    def __init__(self, name, id_number, class_level):
        super().__init__(name, id_number)  # Inheritance
        self.__grades = []                 # Encapsualtion - private


    def daily_activity(self):               # Abstraction - implementation
        return f"{self._name} attends classes and studies"
    
    def add_grade(self, subject, score):
        if 0 <= score <= 100:
            self.__grades.append({"subject": subject, "score" : score}) # Encapsulation
            return f"Grade added: {subject} = {score}"
        return "invalid grade"
    
    def get_average(self):  # Encapsulation - controlled access
        if self.__grades: 
            total = sum(grade["score"] for grade in self.__grades)
            return total / len(self.__grades)   

# Inheritance - Teacher inherits from SchoolMember
class Student(SchoolMember):
    def __init__(self, name, id_number, class_level):
        super().__init__(name, id_number)  # Inheritance
        self.__grades = []                 # Encapsulation - private

    def daily_activity(self):   # Abstraction - implementation
        return f"{self._name} teaches {self.__subject} and grades assignments"
    
    # using all three principles together
student = Student("Adunni Olaleye", "STU001", "SS2")
teacher = Teacher("Mr. Emeka Nwosu", "TCH001", "Mathematics")

print(student.daily_activity())
#print(teacher.daily_activity())
    


# Encapsulation - controlled access to data
print(student.add_grade("Mathematics", 85))  # Grade added: Mathematics = 85
print(student.add_grade("English", 78))      # Grade added: English = 78
print(f"Average: {student.get_average()}")   # Average: 81.5





