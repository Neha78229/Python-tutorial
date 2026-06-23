class student:


    def __init__(self,Rollno,name,percent):
       self.Rollno=Rollno
       self.name=name
       self.percent=percent

   
    def show(self):
        print(f"Rollno:{self.Rollno} Name: {self.name} percent: {self.percent}")



s1=student(101,'Neha','89%')
s2=student(105,'Harshada','78%')
s3=student(103,'Falguni','89%')
s4=student(106,'Akash','56%')
s5=student(110,'Piyush','45%')
print(f"Rollno :{s1.Rollno} Name: {s1.name} Percent: {s1.percent}")


s1.show()
s2.show()
s3.show()
s4.show()