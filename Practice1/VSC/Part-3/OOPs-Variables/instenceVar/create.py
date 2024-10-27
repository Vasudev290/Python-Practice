#Instence Variable - if variable value is varied from object to object 
#How to Create, Read, Update and Delete - instence variable

#How to create :
#inside a constructor - using self. self is pointer, pointing to corrent object.
#inside a instence method - using self variable
#outside a calss, using object ref 

class Employee:
    def __init__(self,id,name):     #Constructor
        self.emp_id = id
        self.emp_name = name
        
    def set_Sal(self,amt):         #instence variable
        self.emp_sal = amt
    
a1= Employee(101,'Arjun')    
a2= Employee(101,'Surya')    

print(a1.__dict__)  #{'emp_id': 101, 'emp_name': 'Arjun'}
print(a2.__dict__)  #{'emp_id': 101, 'emp_name': 'Surya'}

a1.set_Sal(45000)  #Invoking instence variable
a2.set_Sal(55000)

print(a1.__dict__)  #{'emp_id': 101, 'emp_name': 'Arjun', 'emp_sal': 45000}
print(a2.__dict__)  #{'emp_id': 101, 'emp_name': 'Surya', 'emp_sal': 55000}

a1.emp_loc='New Dehli'
a2.emp_loc='New Dehli'  #using object ref to createing

print(a1.__dict__)  #{'emp_id': 101, 'emp_name': 'Arjun', 'emp_sal': 45000, 'emp_loc': 'New Dehli'}
print(a2.__dict__)  #{'emp_id': 101, 'emp_name': 'Surya', 'emp_sal': 55000, 'emp_loc': 'Mumbai'}