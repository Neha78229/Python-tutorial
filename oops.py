#method: Inside a class function is called method
class Employee:

    #constructor
    def __init__(self,id,name,salary):
       self.id=id
       self.name=name
       self.salary=salary

    #reusable method
    def show(self):
        print(f"ID:{self.id} Name: {self.name} Salary: {self.salary}")


#create object of class
e1=Employee(1,'Neha',40000)
e2=Employee(3,'Naina',30000)
e3=Employee(2,'Falguni',10000)
e4=Employee(5,'Akash',20000)
e5=Employee(4,'Piyush',400000)
print(f"ID:{e1.id} Name: {e1.name} Salary: {e1.salary}")


e1.show()
e2.show()
e3.show()
e4.show()