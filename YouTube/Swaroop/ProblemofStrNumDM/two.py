#Grade Calculater
m = int(input("Marks of Maths :"))
s = int(input("Marks of Science :"))
e = int(input("Marks of English :"))

total_marks = m+s+e
average = total_marks/3

percentage = (total_marks/300)*100
grade = ""

if percentage > 90:
    grade ='A'
    
elif percentage > 80 and percentage <= 90:
    grade ='B'
    
elif percentage > 70 and percentage <= 80:
    grade ='C'

else:
    grade = 'Pass'
    
print(f"Total Marks:{total_marks} \nAverage Marks:{average} \nGrade :{grade}")