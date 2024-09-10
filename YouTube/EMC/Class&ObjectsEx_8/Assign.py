#Create a class called student 
#Create a variable = name and register number using constructor. 
#Create a function called display which should display the name and register number of the student.

class student:
    def __init__(self):
        self.name="Govindharaju"
        self.regno='KA 07 CM 2024'
    def display(self):
        print("Name :",self.name)
        print("Reg No :", self.regno)


s1=student()
print(s1.name)
print(s1.regno)
s1.display()