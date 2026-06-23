#Level-wise flow of classes
class Register:
    def reg(self,name,qualification,resume,cgpa):
        print(f"Details: {name} || {qualification} || {resume} || {cgpa}")

class Verfication(Register):
    def verify(self):
        is_eligible=True
        if(is_eligible==True):
            print("You are eligible")
        else:
            print("You are not eligible")

class OfferLetter(Verfication):
    def offer_letter(self):
        print("Congratualations You are Selected ")

m=OfferLetter()
m.reg('Neha','Engineering','myresume.pdf',9.0)
m.verify()
m.offer_letter()
