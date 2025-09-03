

class Student:
    def __init__(self, name, course, level):
        print("creating a new student...")
        self.name = name
        self.course = course
        self.level = level
        print(f"Student {name} has been created!")

kemi = Student("Kemi Adebayo", "Computer Science", 300)



class NigerianStudent:
    def __init__(self, name, state, course):
        print(f"step 1: creating student object...")
        self.name = name  # assigning name to this object
        self.state_of_origin = state # assigning state to this object
        self.course = course #  assigning course to this object
        self.student_id = self.generate_id()   # generate id for this object
        print(f"Step 6: {self.name} from {self.state_of_origin} is ready!")

    def generate_id(self):
        import random
        return f"UNISAIL{random.randint(1000, 9999)}"

ayo = NigerianStudent("Ayo Daniel", "Lagos", "Street Statistics")
print(ayo.name)
print(ayo.student_id)

# creating multiple users

class PhoneUser:
    def __init__(self, name, network):
        self.name = name
        self.network = network
        self.airtime = 0
        print(f"{self.name} joined {self.network} network")

    def buy_airtime(self, amount):
        self.airtime += amount
        return f"{self.name} now has #{self.airtime} airtime"

abeeb = PhoneUser("Abeeb Bakare", "MTN")
onisemo = PhoneUser("Onisemo williams", "Airtel")

print(abeeb.buy_airtime(500))
print(onisemo.buy_airtime(1000))
print(abeeb.airtime)
print(onisemo.airtime)



# Defining Attributes of a student
class Student:
    def __init__(self, name, course, level, state_of_origin):
        self.name = name
        self.course = course
        self.level = level
        self.state_of_origin = state_of_origin
        self.cgpa = 0.0

# creating the student object
Fathia = Student("Fathia Abdul", "Biochemistry", 300, "Ogun state")
print(Fathia.name)
print(Fathia.course)
print(Fathia.state_of_origin)

# Types of Attribute

# Instance Attribute : This is unique to each object

student1 = Student("Anthony Johnson", "Engineering", 200, "Ogun")
student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos")

print(student1.name)
print(student2.name)

# # class attributes : This is shared by all the object

class Student:
    university =  "Federal University of Technology Akure"

    def __init__(self, name, course):
        self.name = name
        self.course = course

print(Student.university)
print(student1.university)
print(student2.university)


# Methods: what object can do

# example : what nigerian student can do?

class Student:
    def __init__(self, name, course, level):
        # Attributes
        self.name = name
        self.course = course
        self.level = level
        self.cgpa = 0.0
        self.fees_paid = False


        # Method: action the student can do
    def pay_school_fee(self):
            self.fees_paid = True
            return f"{self.name} has paid school fees for {self.level} level"
    
        # method: another action

    def register_courses(self):
         if self.fees_paid:
              return f"{self.name} has registered courses for {self.course}"
         else:
              return f"{self.name} must pay school fees first!"
         
         # Method: calculates CGPA

    def calculate_cgpa(self, grades):
         if grades:
              self.cgpa = sum(grades) / len(grades)
              return f"{self.name}'s CGPA is now {self.cgpa:2f}"
         return "No grades provided"
    
    # using

Abiodun = Student("Abiodun Akinola", "Gistology", 600)
    
print(Abiodun.pay_school_fee())
print(Abiodun.register_courses())
print(Abiodun.calculate_cgpa([4.2, 3.8, 4.0, 3.5]))


# Type of methods

# Instance Method : work with specific object
def pay_school_fees(self):
    return f"{self.name} has paid school fess"     

#class Methods: work with class-level data
@classmethod
def get_university(cls):
    return cls.university

# Static Methods
@staticmethod
def academic_calender():
    return "Academic session runs from september to July"
 

class BankAccount:
    def __init__(self, owner, bank_name, balance = 0):
        # Attributes - What the account has
        self.owner = owner
        self.bank_name = bank_name
        self.balance = balance
        self.account_number = self.generate_account_number()

          # Methods - What the account can do
    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.balance += amount  # Method changes attribute
            return f" # {amount:,} deposited to {self.owner}'s {self.bank_name} account. New balance: #{self.balance:,} "
        return "invalid deposit amount"
    
    def withdraw(self, amount):
        """Remove money from the account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"#{amount:,} withdrawn from {self.owner}'s account. New balance: #{self.balance} "
        return "Insufficient funds or invalid amount"

    def transfer(self,amount, recipient):
        """ Transfer money to another account"""
        if amount > 0 and amount <=self.balance:
            self.balance -= amount
            return f" #{amount:,} transfered to {recipient}. Remaining balance: #{self.balance:,} " 
        return "Transfer failed: Insufficient funds"
            
    def check_balance(self):
        """ check current balance """
        return f"{self.owner}'s {self.bank_name} account balance: #{self.balance:,}"

    def generate_account_number(self):
        """Generate a unique account number"""
        import random
        return f"01{random.randint(10000000, 99999999)}"
    
    # creating and using the account
adunni_account = BankAccount("Adunni Olaleye", "AXT Bank", 50000)

# Attributes(characteristics)
print(f"owner: {adunni_account.owner}")
print(f"Bank: {adunni_account.bank_name}")
print(f"Account Number: { adunni_account.account_number}")


# Methods (actions)
print(adunni_account.deposit(25000))
print(adunni_account.withdraw(10000))
print(adunni_account.transfer(15000, "Sunday James"))
print(adunni_account.check_balance())


# Practice Exercise


class NaijaPhone:
    # Attribute
    def __init__(self, brand, model, network_provider):
        self.brand = brand
        self.model = model
        self.network_provider = network_provider
        self.airtime_balance = 0
        self.data_balance = 0
        self.is_on = False
    # Methods
    def power_on(self):
        self.is_on = True
        return f"{self.brand} phone is now on. Network:{self.network_provider} "
    
    def buy_airtime(self, amount):
        self.airtime_balance += amount
        return f"#{amount} airtime purchased. Balance: #{self.airtime_balance}"
    
    def make_call(self, number):
        if self.is_on and self.airtime_balance > 0:
            self.airtime_balance -= 10
            return f"Calling {number}.... Remaining airtime: #{self.airtime_balance}"
        return "Cannot make call Check phone power and airtime balance"
    
    def send_sms(self, message, number):
        if self.airtime_balance > 4:
            self.airtime_balance -= 4
            return f"SMS sent to {number}: '{message}'. Remaining airtime: #{self.airtime_balance}"
        return "Insufficient airtime to send SMS"
    

 # creating and using the phone
yemi_phone = NaijaPhone("Tecno", "spark_9", "MTN")


#Attributes(characteristics)
print(f"Brand: {yemi_phone.brand}")
print(f"Model: {yemi_phone.model}")
print(f"Network Provider: { yemi_phone.network_provider}")


# Methods (actions)
print(yemi_phone.power_on())
print(yemi_phone.buy_airtime(100))
print(yemi_phone.make_call("08109155294"))
print(yemi_phone.send_sms("Thanks for the visitation", "08109155294"))



# Practice Exercise 2

class BRTBus:
    def __init__(self, route, bus_number):

       # Attributes 
        self.route = route
        self.bus_number = bus_number
        self.current_stop = "Ikorodu"
        self.passenger_count = 0
        self.fare = 300

    # Methods

    def announce_stop(self):
        return f"Next stop: {self.current_stop}. Fare is #{self.fare}"
    
    def board_passenger(self, count):
        self.passenger_count += count
        return f"{count} passengers boarded. Total: {self.passenger_count}"
    

#  # creating and using the BRTBus
danfo = BRTBus("yaba", "bus number")
# # Methods (actions)
print(danfo.announce_stop())
print(danfo.board_passenger(5))


#Practice Exercise 3

class MarketTrader:
    def __init__(self, name, market_name, goods):
        
      # Attribute
        self.name = name
        self.market_name = market_name
        self.goods = goods
        self.daily_sales = 0
      
      # Method
    def advertise_goods(self):
        return f"{self.name} at {self.market_name}: Fresh {"".join(self.goods)} available!"

    def make_sale(self, amount):
        self.daily_sales += amount
        return f"Sale made! Today's total: #{self.daily_sales:,}"
    
# #  # creating and using the MarketTrader
Market = MarketTrader("yemi", "Oyingbo", "shoes")
    
    # Methods (actions)
print(Market.advertise_goods())
print(Market.make_sale(500))


