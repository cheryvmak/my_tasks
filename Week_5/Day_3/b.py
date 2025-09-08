
class NigerianBankAccount:
    def __init__(self, owner, initial_balance = 0):

        self.owner = owner
        self._balance = initial_balance   # Protected attribute
        self.__pin = "1234"     # private attribute
        self._transaction_history = []  # Protected attribute


    def deposit (self, amount):
            if amount > 0:
                self._balance += amount
                self._transaction_history.append(f"Deposited #{amount:,}")
                return f"#{amount:,} deposited successfully"
            return "Invalid deposit amount"
        
    def withdraw(self, amount, pin):
            if self.__verify_pin(pin): # private method
                if amount <= self._balance:
                    self._balance -= amount
                    self._transaction_history.append(f"withdrew #{amount:,}")
                    return f"#{amount:,} withdrawn succesfully"
                return "Insufficient funds"
            return "Invalid PIN"
        
    def check_balance(self, pin):
            if self.__verify_pin(pin):
                return f"Current balance: #{self._balance:,}"
            return "Invalid PIN"
        
        # Private method - only the class can use this
        
    def __verify_pin(self, entered_pin):
            return entered_pin == self.__pin
        
        #Protected method - subsclasses can use this

    def _get_transaction_history(self):
            return self._transaction_history.copy()
        

# Using the encapsulated account
ibrahim_account = NigerianBankAccount("Ibrahim Orekunrin", 50000)

# These work - public interface
print(ibrahim_account.deposit(10000))
print(ibrahim_account.withdraw(5000, "1234"))
print(ibrahim_account.check_balance("1234"))
print(ibrahim_account._get_transaction_history())


print(ibrahim_account.__verify_pin("1234"))   # This will result in error due to private method


# Abstraction


from abc import ABC, abstractmethod

# Abstract base class - defines what a Nigerian student should do

class NigerianStudent(ABC):
    def __init__(self, name, course, level):
        self.name = name
        self.course = course
        self.level = level
        self.fees_paid = False

    # Concrete method - all student can do this
    def pay_school_fees(self, amount):
        self.fees_paid = True
        return f"{self.name} paid #{amount:,} school fees"
    
    # Abstract method - each type of student implements differently
    @abstractmethod
    def study_method(self):
        pass

    @abstractmethod
    def take_exam(self):
        pass

    # Concrete classes - specific implementations
class MedicalStudent(NigerianStudent):
    def study_method(self):
        return f"{self.name} studies anatomy books and practices on cadavers"
    
    def take_exam(self):
        return f"{self.name} takes practical exam in the anatomy lab"
    
class EngineeringStudent(NigerianStudent):
    def study_method(self):
        return f"{self.name} solves mathematical problems and builds prototypes"
    
    def take_exam(self):
        return f"{self.name} takes exam with calculations and technical drawings"
    
class ComputerScienceStudent(NigerianStudent):
    def study_method(self):
        return f"{self.name} codes program and debugs software"
    
    def take_exam(self):
        return f"{self.name} takes practical programming exam on computer"
    

# Using Abstraction 

students = [
    MedicalStudent("Dr.Adeyinka Ogunsanya", "Medicine", 400),
    EngineeringStudent("Dr. Ajala Gift", "Mechanical Engineering", 300),
    ComputerScienceStudent("Fatima Hassan", "Computer Science", 200)

]

# Same interface, different implementations
for student in students:
    print(student.pay_school_fees(150000))
    print(student.study_method())
    print(student.take_exam())
    print("---")


#Simple abstraction for phone interface

class SimplePhone:
    def __init__(self, brand):
        
        self.brand = brand
        self.complex_internal_system = "Very complicated stuff"

 # Simple interface - user doesn't need to know internal complexity
    def make_call(self, number):
        self._establish_network_connection()
        self._encode_voice_signal()
        self._transmit_to_tower()
        return f"Calling {number} from {self.brand} phone..."

    def send_sms(self, message, number):
        self._connect_to_sms_center()
        self._format_message()
        self._send_through_network()
        return f"SMS sent to {number}: {message}"
    
    # Complex internal methods - hidden from user
    def _establish_network_connection(self):
        # Complex networking code here
        pass

    def _encode_voice_signal(self):
        # Complex networking code here
        pass

    def _transmit_to_tower(self):
        # Complex networking code here
        pass
    
    def _connect_to_sms_center(self):
        # Complex networking code here
        pass

    def _format_message(self):
     # Complex networking code here
     pass

    def _send_through_network(self):
     # Complex networking code here
     pass


# User only needs to know the simple interface
my_phone = SimplePhone("Tecno")

print(my_phone.make_call("08109155291"))
print(my_phone.send_sms("Thank you!","0810914423"))




# Inheritance

# Parent class - Base Nigerian Person
class NigerianPerson:
    def __init__(self, first_name, last_name, state_of_origin):
        self.first_name = first_name
        self.last_name = last_name
        self.state_of_origin = state_of_origin
        self.can_speak_english = True

    def introduce(self):
        return f"My name is {self.first_name} {self.last_name} from {self.state_of_origin}"
    
    def greet(self):
        return f"Good morning!"
    
    def speak_local_language(self):
        return "I speak my local language"
    
    # Child class 1 - Nigerian Student inherits from NigerianPerson
class NigerianStudent(NigerianPerson):
    def __init__(self, first_name, last_name, state_of_origin, course, level):
         
         # Inherit parent's initialization
        super().__init__(first_name, last_name, state_of_origin)
          
          # Add student-specific attributes
        self.course = course
        self.level = level
        self.cgpa = 0.0

        # Override parent method with student-specific version
    def introduce(self):
        parent_intro = super().introduce() # Get parent introduction
        return f"{parent_intro}. I'm a {self.level} level {self.course} student"
       
       # Add student-specific methods
    def study(self):
        return f"{self.first_name} is studying {self.course}"
    
    def take_exam(self):
        return f"{self.first_name} is writting {self.course} exam"
    
    # Child class 2 - Nigerian Worker inherits from NigerianPerson
class NigerianWorker(NigerianPerson):
    def __init__(self, first_name, last_name, state_of_origin, job_title, company):

        super().__init__(first_name, last_name, state_of_origin)
        self.job_title = job_title
        self.company = company
        self.salary = 0

    def introduce(self):
        parent_intro = super().introduce()
        return f"{parent_intro}. I work as a {self.job_title} at {self.company}"
    
    def work(self):
        return f"{self.first_name} is working as a {self.job_title}"
    
    def receive_salary(self, amount):
        self.salary += amount
        return f"{self.first_name} received #{amount:,} salary"
    
    # Child class 3 - Nigerian Teacher (inherits from NigerianWorker)
class NigerianTeacher(NigerianWorker):
    def __init__(self, first_name, last_name, state_of_origin, subject, school):

         # Teacher is a type of worker
         super().__init__(first_name, last_name, state_of_origin, "Teacher", school)
         self.subject = subject
         self.students = []

    def introduce(self):
        return f"My name is {self.first_name} {self.last_name} from {self.state_of_origin}. I teach {self.subject} at {self.company}"

    def teach(self):
        return f"Teacher {self.first_name} is teaching {self.subject}"
    
    def grade_students(self):
        return f"Teacher {self.first_name} is grading {self.subject} assignments"
    
#Using inheritance
#Create different types of people

student = NigerianStudent("kemi", "Adetiba","ogun state", "sts",400)
worker = NigerianWorker("Adeola", "Oluyemi", "ogun state", "Software Engineer", "liquid Lab")
teacher = NigerianTeacher("Wale", "Adedayo","ogun state", "Mathematics", "UNIgen")

# print(student.introduce())
# print(worker.introduce())
# print(teacher.introduce())

# All inherit basic Nigerian person abilities
print("=== Basic Inherited Methods ===")
print(student.greet())                    # Good morning! (inherited)
print(worker.speak_local_language())      # I speak my local language (inherited)
print(teacher.greet())                    # Good morning! (inherited)

print("\n=== Customized Introductions ===")
print(student.introduce())    # Customized for students
print(worker.introduce())     # Customized for workers  
print(teacher.introduce())    # Customized for teachers

print("\n=== Specific Abilities ===")
print(student.study())        # Only students can do this
print(worker.work())          # Only workers can do this
print(teacher.teach())        # Only teachers can do this



# Types of inheritance

# single inheritance
class Parent:
    pass
class Child(Parent):
    pass


# multiple inheritance
class Father:
    def father_trait(self):
        return "strong"
class Mother:
    def mother_trait(self):
        return "Caring"
class Child(Father, Mother):
    pass 

child = Child()
print(child.father_trait())
print(child.mother_trait())

