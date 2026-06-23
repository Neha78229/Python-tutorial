#hierarchical inheritance :When a single base class inherit into two or more class is called Hierarchical 
#Inheritance.

class HRM:
    def emp_reg(self,id,name,date_joining,salary):
        
        print(f"Id: {id} Name: {name} Date of Joining:{date_joining} || Salary:{salary}")

    def login(self,Intime):
        pass

    def logut(self,OutTime):
        pass

class Manager(HRM):
        def login(self,Intime):
         print(f"In time: {Intime}")

        def logut(self,OutTime):
         print(f"Out Time:{OutTime} ")


class Employee(HRM):
        def login(self,Intime):
         print(f"In time: {Intime}")

        def logout(self,OutTime):
         print(f"Out Time:{OutTime} ")
         

h1=HRM()
h2=HRM()
h3=HRM()

m=Manager()
e=Employee() 


print("---------------All Employees----------------------")
h1.emp_reg(1,'Neha','23/6/2025',25000)
h2.emp_reg(2,'Falguni','23/6/2025',25000)
h3.emp_reg(3,'Harshada','23/6/2025',25000)

print("-------------Manager Details------------------------")
m.emp_reg(1,'Neha','25/07/2032',5000000)
m.login("9:00 AM")
m.logut("9:00 PM")

print("---------------Employee Details----------------------")
#employee
e.emp_reg(3,"Harshada",'23/6/2025',25000)
e.login("9:00 AM")
e.logout("5:00 PM")