#Inheritance: When inheirt data of one class(super class or base class) into 
# another(sub-class or derived class) is called inheritance.

class HSC:
    def hsc_details(self):
        name="Neha"
        stream="Science"
        print(f"{name} || {stream} ")

#single Inheritance
class Grduation(HSC):
    def info(self):
        branch="science"
        if(branch=="science"):
            print("Engineering")
        elif(branch=="commerce"):
            print("B.com || CA")
        elif(branch=="Arts"):
            print("Teacher")

g=Grduation()
g.hsc_details()
g.info()  